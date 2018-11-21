#!/usr/bin/env python

from operator import itemgetter 
import sys

# keep a map of the sum of upvotes of each reddit
genre_map = {}
genre_map_1={}

for segment in sys.stdin:
    segment = segment.strip()
    title, user_count, genre_rating = segment.split('\t', 2) #splitting the data arrays into the three different columns 
    title_1=title
    try:
    	user_count = int(user_count)
        genre_rating=float(genre_rating)
        # print(count{0})
        # print(reddit)nre
        genre_map[title] = genre_map.get(title, 0) + genre_rating  ##mapping for ratings 
        if user_count==1:
        	genre_map_1[title_1] = genre_map_1.get(title_1, 0) + user_count  # mapping for number of users who have voted
        
    except ValueError:
    #    ignore lines where the count is not a number
        pass

# sort the reddits alphabetically;
sorted_genre_map = sorted(genre_map.items(), key=itemgetter(0))
sorted_genre_map_1 = sorted(genre_map_1.items(), key=itemgetter(0))
dic1=sorted_genre_map
dic2=sorted_genre_map_1
average_rate=[]
for i in range(len(dic1)):
	average_rate= average_rate + [(dic1[i][1]/dic2[i][1])]
for i in range(len(dic1)):
	print '%s\t%s\t%s'% (dic1[i][0],dic2[i][1],average_rate[i])


 