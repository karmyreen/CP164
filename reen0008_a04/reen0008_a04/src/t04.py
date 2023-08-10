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

from utilities import array_to_queue, queue_to_array
queue = Queue()


list = []

source1 = Queue()
source2 = Queue()
l1 = [8, 10, 8, 9]
l2 = [7, 9]

array_to_queue(source1, l1)
array_to_queue(source2, l2)


queue.combine(source1, source2)
queue_to_array(queue, list)


print(list)
