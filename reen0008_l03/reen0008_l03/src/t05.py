"""
-------------------------------------------------------
CP164 
-------------------------------------------------------
Author:  Gurkarman Reen
ID:      169030008
Email:   reen0008@mylaurier.ca
__updated__ = "2023-02-04"
-------------------------------------------------------
"""
# Imports
from Priority_Queue_array import Priority_Queue

queue = Priority_Queue()

qlist = [5, 4, 3, 10, 11]

for i in qlist:
    queue.insert(i)

for i in queue:
    print(i)


queue.remove()
print()

for i in queue:
    print(i)


# Constants
