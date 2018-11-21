#!/usr/bin/env python

from operator import itemgetter 
import sys

# keep a map of the sum of upvotes of each reddit
genremap = {}
genremap_1={}

for line in sys.stdin:
    line = line.strip()
    title, count, rating = line.split('\t', 2)
    title_1=title
    try:
    	count = int(count)
        rating=float(rating)
        # print(count{0})
        # print(reddit)
        genremap[title] = genremap.get(title, 0) + rating
        if count==1:
        	genremap_1[title_1] = genremap_1.get(title_1, 0) + count
        
    except ValueError:
    #    ignore lines where the count is not a number
        pass

# sort the reddits alphabetically;
alphabetic_genremap = sorted(genremap.items(), key=itemgetter(0))
alphabetic_genremap_1 = sorted(genremap_1.items(), key=itemgetter(0))
d1=alphabetic_genremap
d2=alphabetic_genremap_1
avr_rating=[]
for i in range(len(d1)):
	avr_rating= avr_rating + [(d1[i][1]/d2[i][1])]
for i in range(len(d1)):
	print '%s\t%s\t%s'% (d1[i][0],d2[i][1],avr_rating[i])


 