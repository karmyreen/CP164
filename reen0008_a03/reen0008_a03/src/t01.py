"""
-------------------------------------------------------
CP164 
-------------------------------------------------------
Author:  Gurkarman Reen
ID:      169030008
Email:   reen0008@mylaurier.ca
__updated__ = "2023-02-05"
-------------------------------------------------------
"""
# Imports

from Stack_array import Stack
from functions import stack_split_alt

stack = Stack()

l1 = [-1, -2, -3, 4, 6, 0]

for i in l1:
    stack.push(i)

for i in stack:
    print(i)


print()

target1, target2 = stack_split_alt(stack)

for i in target1:
    print(i)


print()

for i in target2:
    print(i)


# Constants
