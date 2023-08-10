"""
-------------------------------------------------------
CP164 
-------------------------------------------------------
Author:  Gurkarman Reen
ID:      169030008
Email:   reen0008@mylaurier.ca
__updated__ = "2023-03-31"
-------------------------------------------------------
"""
# Imports

# Constants
from test_Sorts_array import test_sort, SORTS

header1 = "n:   100               |      Comparisons       | |         Swaps          |"
header2 = "Algorithm              In Order Reversed   Random In Order Reversed   Random"
header3 = "--------------         -------- -------- -------- -------- -------- --------"

print(header1)
print(header2)
print(header3)
for i in SORTS:
    test_sort(i[0], i[1])
