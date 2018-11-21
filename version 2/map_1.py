#The function uses MAPREDUCE functions of HDFS
import sys

for segment in sys.stdin: #read input lines from CSV file
    segment = segment.strip()
    sections = segment.split(',') # split line into parts
    # print(columns[2])	
    movie_genres = sections[2].split('|')
    # print(len(genres))
    # print(len(genres))
    if len(sections) == 3: ##making sure that only correct data is manipulated
     	try:    ##try catch exception handling
     		count_genre = 1
     		for i in range(7): #we know that there are not more than 8 genres 
     			print "%s\t%s" % (str(movie_genres[i]),count_genre)	 
     				# print(len(genres[i]))
     	except (ValueError,IndexError):
     		pass