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

source1 = [int(i) for i in input(
    "Enter values: ").split(",")]

stack = Stack()

array_to_stack(stack, source1)
stack = list(map(int, stack))
print("Stack: ", stack)
print("source: ", source1)


# Constants
