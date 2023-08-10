"""
-------------------------------------------------------
CP164 
-------------------------------------------------------
Author:  Gurkarman Reen
ID:      169030008
Email:   reen0008@mylaurier.ca
__updated__ = "2023-04-06"
-------------------------------------------------------
"""
# Imports
from List_linked import List
from Sorts_List_linked import Sorts
lst = List()

lst.append(5)
lst.append(10)
lst.append(9)
lst.append(33)
lst.append(21)


Sorts.radix_sort(lst)


for i in lst:
    print(i)

# Constants
