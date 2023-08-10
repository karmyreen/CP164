"""
-------------------------------------------------------
CP164 
-------------------------------------------------------
Author:  Gurkarman Reen
ID:      169030008
Email:   reen0008@mylaurier.ca
__updated__ = "2023-01-22"
-------------------------------------------------------
"""
# Imports
from functions import shift


name1 = "peele.txt"
name2 = "shift.txt"

fh1 = open(name1, 'r')
fh2 = open(name2, 'w')

for i in fh1:
    answer = shift(i, 1)
    fh2.write(answer)


fh1.close()
fh2.close()
