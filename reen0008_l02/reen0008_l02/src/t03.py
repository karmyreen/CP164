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


from utilities import array_to_stack
from Stack_array import Stack


stack = Stack()
source = [-1, -6, 7, -99, 9, 10]


array_to_stack(stack, source)

for i in stack:
    print(i)
