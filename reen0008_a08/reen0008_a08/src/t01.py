"""
-------------------------------------------------------
CP164 
-------------------------------------------------------
Author:  Gurkarman Reen
ID:      169030008
Email:   reen0008@mylaurier.ca
__updated__ = "2023-03-27"
-------------------------------------------------------
"""
# Imports

# Constants
# Imports
from BST_linked import BST
# Constants

print("_eq__")
bst = BST()

for val in [10, 24, 7, 25, 13, 23]:
    bst.insert(val)

print("BST 1: ")
for i in bst:
    print(i)

bst2 = BST()

for val in [12, 1, 16, 34, 94]:
    bst2.insert(val)

print("BST 2 ")
for k in bst2:
    print(k)

print(" ")

print("BSTs equal? ", bst == bst2)

print(" ")
print("s_balanced")
b = bst.is_balanced()
print("Is BST balanced? ", b)

print(" ")

b = bst.is_valid()
print("Is BST valid? ", b)

print(" ")
print("--min--")
value = bst.min()
print("Min value in BST: ", value)

print(" ")
print("leaf_count")
count = bst.leaf_count()
print("Number of leaves in BST: ", count)

print(" ")
print("one_child_count")
count = bst.one_child_count()
print("One child count: ", count)

print(" ")
print("two_child_count")
count = bst.two_child_count()
print("Two child count: ", count)

print(" ")
print("inorder")
print("Inorder traversal: ")
for i in bst.inorder():
    print(i)

print(" ")
print("preorder")
print("Preorder traversal: ")
for i in bst.preorder():
    print(i)

print(" ")
print("postorder")
print("Postorder traversal: ")
for i in bst.postorder():
    print(i)

print(" ")
print("remove")
key = 11
print("Key: ", key)
bst.remove(key)
print("BST after removing: ")
for i in bst:
    print(i)
