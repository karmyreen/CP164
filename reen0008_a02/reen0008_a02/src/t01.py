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
from Movie_utilities import get_by_year, read_movies
name = "movies.txt"

fh = open(name, 'r')


ymovies = get_by_year(read_movies(fh), 2005)

for i in range(len(ymovies)):
    print(ymovies[i])
    print()


fh.close()
# Constants
