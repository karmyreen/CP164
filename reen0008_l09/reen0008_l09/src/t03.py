"""
-------------------------------------------------------
CP164 
-------------------------------------------------------
Author:  Gurkarman Reen
ID:      169030008
Email:   reen0008@mylaurier.ca
__updated__ = "2023-03-23"
-------------------------------------------------------
"""
# Imports
from Hash_Set_array import Hash_Set


hs = Hash_Set(10)

hs.insert(5)
hs.insert(6)
hs.insert(7)
hs.insert(11)


# hs.debug()

hs._rehash()


# Constants
