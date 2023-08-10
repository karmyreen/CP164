"""
-------------------------------------------------------
CP164 
-------------------------------------------------------
Author:  Gurkarman Reen
ID:      169030008
Email:   reen0008@mylaurier.ca
__updated__ = "2023-04-03"
-------------------------------------------------------
"""
# Imports

from BST_linked import BST


bst = BST()

for val in [10, 24, 7, 25, 13, 23]:
    bst.insert(val)

val = 24 in bst

print(val)

print()

zero, one, two = bst.node_counts()


print(f"{zero},{one},{two}")


# Constants
