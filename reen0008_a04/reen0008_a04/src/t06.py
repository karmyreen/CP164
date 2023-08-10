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
source = Priority_Queue()


l1 = [7, 5, 1, 4, 100, 21, 6, 10, 100, 400, 500]
list1 = []
list2 = []

array_to_pq(source, l1)
key = 23
print(f"Key: {key}")
target1, target2 = source.split_key(key)


pq_to_array(target1, list1)
pq_to_array(target2, list2)

print(list1)
print()
print(list2)


# Constants
