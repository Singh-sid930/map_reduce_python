#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip()
    columns = line.split(',') # split line into parts
    # print(columns[1])
    if len(columns) == 4: 
     	try:
            count = 1
            count_ratings=float(columns[2])
            print "%s\t%s\t%s" % (columns[1],int(count),count_ratings)
        except (ValueError,IndexError):
            pass