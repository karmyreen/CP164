"""
-------------------------------------------------------
CP164 
-------------------------------------------------------
Author:  Gurkarman Reen
ID:      169030008
Email:   reen0008@mylaurier.ca
__updated__ = "2023-04-05"
-------------------------------------------------------
"""
# Imports

from Sorts_array import Sorts
lst = [90, 10, 2, 4, 8, 11, 5, 17]

Sorts.radix_sort(lst)


print()
for i in lst:
    print(f"{i}", end=" ")
