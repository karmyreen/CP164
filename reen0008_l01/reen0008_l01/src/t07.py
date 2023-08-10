"""
-------------------------------------------------------
CP164 
-------------------------------------------------------
Author:  Gurkarman Reen
ID:      169030008
Email:   reen0008@mylaurier.ca
__updated__ = "2023-01-20"
-------------------------------------------------------
"""
# Imports
from Movie_utilities import read_movies


name = "movies.txt"


fv = open(name, 'r')

movie = read_movies(fv)
print(movie)
for line in movie:

    print(line)
    print()


fv.close()


# Constants
