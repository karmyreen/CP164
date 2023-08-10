"""
-------------------------------------------------------
CP164 
-------------------------------------------------------
Author:  Gurkarman Reen
ID:      169030008
Email:   reen0008@mylaurier.ca
__updated__ = "2023-01-21"
-------------------------------------------------------
"""
# Imports

from functions import file_analyze

name = "movies.txt"

fv = open(name, 'r+')

u, l, w, d, r = file_analyze(fv)

print(f"{u},{l},{w},{d},{r}")

fv.close()


# Constants
