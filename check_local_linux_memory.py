#!/usr/bin/env python
#
# -*- coding: utf-8 -*-
#
#   Autors: David Hannequin <david.hannequin@gmail.com>,
#   Date: 2017-02-17
#   URL: 
#   
#   Plugins to check linux memory usage.
#
# Shinken plugin is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Shinken plugin is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Shinken.  If not, see <http://www.gnu.org/licenses/>.
#
# Requires: Python >= 2.7 

import argparse
import psutil

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', '--warning', default='80', help='Warning thresold')
    parser.add_argument('-c', '--critical', default='90', help='Critical thresold')

    args = parser.parse_args()

    warning = args.warning
    critical = args.critical
    
    return warning,critical

def kb_to_mb(num):
    num /= 1024.0
    num /= 1024.0

    return "%.1f" % (num)

def get_data():
    memory_info = psutil.virtual_memory()
    total = memory_info.total
    available = memory_info.available
    percent = memory_info.percent
    used = memory_info.used
    active = memory_info.active
    inactive = memory_info.inactive

    total = kb_to_mb(total)
    available = kb_to_mb(available)
    used = kb_to_mb(used)
    active = kb_to_mb(active)
    inactive = kb_to_mb(inactive)
    return total,available,percent,used,active,inactive

def main():

    warning = parse_args()
    critical = parse_args()

    total,available,percent,used,active,inactive = get_data()

    if percent >= critical:
        print ('CRITICAL - Memory usage: %2.1f%% |mem=%s' % (percent, percent))
        raise SystemExit(2)
    elif percent >= warning:
        print ('WARNING - Memory usage: %2.1f%% |mem=%s' % (percent, percent))
        raise SystemExit(1)
    else:
        print ('OK - Memory usage: %2.1f%% |mem=%s' % (percent, percent))
        raise SystemExit(0)

if __name__ == "__main__":
    main()
