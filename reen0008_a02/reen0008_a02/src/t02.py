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

from Movie_utilities import get_by_rating, read_movies

name = "movies.txt"
fh = open(name, 'r')


rmovies = get_by_rating(read_movies(fh), 8.5)

for i in range(len(rmovies)):
    print(rmovies[i])
    print()

fh.close()

# Constants
