"""
-------------------------------------------------------
CP164 
-------------------------------------------------------
Author:  Gurkarman Reen
ID:      169030008
Email:   reen0008@mylaurier.ca
__updated__ = "2023-04-06"
-------------------------------------------------------
"""
from Sorts_Deque_linked import Sorts
from Deque_linked import Deque


a1 = [55, 56, 54, 55, 21, 4]
a = Deque()
for v in a1:
    a.insert_rear(v)


Sorts.gnome_sort(a)
for v in a:
    print(v)
