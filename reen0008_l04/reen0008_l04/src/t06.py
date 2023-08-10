"""
-------------------------------------------------------
CP164 
-------------------------------------------------------
Author:  Gurkarman Reen
ID:      169030008
Email:   reen0008@mylaurier.ca
__updated__ = "2023-02-10"
-------------------------------------------------------
"""
# Imports

from utilities import list_test
from Movie_utilities import read_movies


name = "movies.txt"

fh = open(name, "r")

lst_movies = read_movies(fh)

list_test(lst_movies)


fh.close()


# Constants
