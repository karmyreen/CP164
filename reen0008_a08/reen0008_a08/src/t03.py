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
from BST_linked import BST
from functions import do_comparisons, letter_table
from Letter import check


DATA1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DATA2 = "MFTCJPWADHKNRUYBEIGLOQSVXZ"
DATA3 = "ETAOINSHRDLUCMPFYWGBVKJXZQ"

bst1, bst2, bst3 = BST(), BST(), BST()
check(bst1, DATA1), check(bst2, DATA2), check(bst3, DATA3)

fv = open("gibbon.txt", "r")
do_comparisons(fv, bst1)

letter_table(bst1)
