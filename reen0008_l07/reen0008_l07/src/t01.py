"""
-------------------------------------------------------
CP164 
-------------------------------------------------------
Author:  Gurkarman Reen
ID:      169030008
Email:   reen0008@mylaurier.ca
__updated__ = "2023-03-10"
-------------------------------------------------------
"""
# Imports
from List_linked import List

lst1 = List()
lst2 = List()


lst1.append(5)
lst1.append(3)
lst1.append(1)
lst1.append(10)

lst2.append(5)
lst2.append(3)
lst2.append(1)
lst2.append(10)

answer = lst1.is_identical_r(lst2)
print(answer)


# Constants
