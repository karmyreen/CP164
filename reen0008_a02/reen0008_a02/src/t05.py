"""
-------------------------------------------------------
CP164 
-------------------------------------------------------
Author:  Gurkarman Reen
ID:      169030008
Email:   reen0008@mylaurier.ca
__updated__ = "2023-01-28"
-------------------------------------------------------
"""
# Imports


from Movie_utilities import genre_counts, read_movies


name = "movies.txt"
fh = open(name, 'r')


answer = genre_counts(read_movies(fh))

print(answer)


fh.close()

# Constants
