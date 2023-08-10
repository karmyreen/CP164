"""
-------------------------------------------------------
CP164 
-------------------------------------------------------
Author:  Gurkarman Reen
ID:      169030008
Email:   reen0008@mylaurier.ca
__updated__ = "2023-01-27"
-------------------------------------------------------
"""
# Imports


from Movie_utilities import read_movies
from Stack_array import Stack


name = "movies.txt"


fh = open(name, 'r')


movies = read_movies(fh)

stack = Stack()

for i in movies:
    stack.push(i)


for i in stack:
    print(i)
    print()


fh.close()


# Constants
