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
from Movie_utilities import get_by_genre, read_movies

name = "movies.txt"
fh = open(name, 'r')

gmovies = get_by_genre(read_movies(fh), 0)

for i in range(len(gmovies)):
    print(gmovies[i])
    print()

# Constants
