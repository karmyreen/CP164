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


# Constants

from Stack_array import Stack


stack = Stack()

l1 = [100, -5, 17, 29, -10, 16, 19, -20]

for i in l1:
    stack.push(i)

for i in stack:
    print(i)


print()


target1, target2 = stack.split_alt()

for i in target1:
    print(i)


print()

for i in target2:
    print(i)
