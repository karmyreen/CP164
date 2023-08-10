"""
-------------------------------------------------------
CP164 
-------------------------------------------------------
Author:  Gurkarman Reen
ID:      169030008
Email:   reen0008@mylaurier.ca
__updated__ = "2023-03-04"
-------------------------------------------------------
"""
# Imports
from List_linked import List

lst = List()

lst.append(5)
lst.append(8)
lst.append(7)
lst.append(10)

key = 5

i = 2

lst.insert(i, key)


for i in lst:
    print(i)
    print()
