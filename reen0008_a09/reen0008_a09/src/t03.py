"""
-------------------------------------------------------
CP164 
-------------------------------------------------------
Author:  Gurkarman Reen
ID:      169030008
Email:   reen0008@mylaurier.ca
__updated__ = "2023-04-02"
-------------------------------------------------------
"""
# Imports
from Hash_Set_BST import Hash_Set

from functions import insert_words, comparison_total

hs = Hash_Set(20)

fv = open("gibbon.txt", "r")


insert_words(fv, hs)

total, max_word = comparison_total(hs)

print(f"Using array-based list Hash_Set")
print(f"Total Comparisons:{total}")
print(
    f"Word with maximum comparisons '{max_word.word}', {max_word.comparisons}")

fv.close()

# Constants
