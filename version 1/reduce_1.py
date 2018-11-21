#!/usr/bin/env python

from operator import itemgetter 
import sys


genremap = {}

for line in sys.stdin:
    line = line.strip()
    title, count = line.split('\t', 1)
    try:
        count = int(count)
        genremap[title] = genremap.get(title, 0) + count
    except ValueError:
        # ignore lines where the count is not a number
        pass

# sort the reddits alphabetically;
alphabetic_genremap = sorted(genremap.items(), key=itemgetter(0))

# output to STDOUT
for title, count in alphabetic_genremap:
    print '%s\t%s'% (title, count)