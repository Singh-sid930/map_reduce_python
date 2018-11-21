#!/usr/bin/env python

from operator import itemgetter 
import sys


genre_map = {}

for segment in sys.stdin:
    segment = segment.strip()
    genre_title, genre_count = segment.split('\t', 1)
    try:
        genre_count = int(genre_count)
        genre_map[genre_title] = genre_map.get(genre_title, 0) + genre_count
    except ValueError:
        # ignore lines where the count is not a number
        pass

# sort the genres alphabetically;
sorted_genre_map = sorted(genre_map.items(), key=itemgetter(0))

# output to STDOUT
for title, values in sorted_genre_map:
    print '%s\t%s'% (title, values)