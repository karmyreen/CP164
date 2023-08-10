"""
-------------------------------------------------------
CP164 
-------------------------------------------------------
Author:  Gurkarman Reen
ID:      169030008
Email:   reen0008@mylaurier.ca
__updated__ = "2023-02-12"
-------------------------------------------------------
"""
# Imports

from Priority_Queue_array import Priority_Queue
from utilities import array_to_pq, pq_to_array
from functions import pq_split_key


pq = Priority_Queue()

l1 = [1, 5, 2, 4, 4, 2, 6, 10, 11]
list1 = []
list2 = []

array_to_pq(pq, l1)
key = 7
print(f"Key: {key}")
r1, r2 = pq_split_key(pq, key)

pq_to_array(r1, list1)
pq_to_array(r2, list2)

print(list1)
print()
print(list2)


# Constants
