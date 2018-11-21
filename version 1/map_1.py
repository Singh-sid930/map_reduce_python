#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip()
    columns = line.split(',') # split line into parts
    # print(columns[2])	
    genres = columns[2].split('|')
    # print(len(genres))
    # print(len(genres))
    # the data is messy, only read those having correct column count
    if len(columns) == 3: 
     	try:
     		count = 1
     		for i in range(8):
     			if genres[i].isalpha():
     				print "%s\t%s" % (str(genres[i]),int(count))
     				# print(len(genres[i]))
     	except (ValueError,IndexError):
     		pass