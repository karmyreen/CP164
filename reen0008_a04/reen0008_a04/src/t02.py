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

from Queue_array import Queue

from utilities import array_to_queue


l1 = [5, 4, 3, 100, 100]
l2 = [5, 4, 3, 100, 100]

source = Queue()
q2 = Queue()


array_to_queue(source, l1)
array_to_queue(q2, l2)

equals = source == q2

print(equals)


# Constants
