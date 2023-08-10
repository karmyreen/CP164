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
from functions import queue_combine
from Queue_array import Queue


source1 = Queue()
source2 = Queue()
l1 = [2, 2, 32, 8]
l2 = [14, 10]

for i in l1:
    source1.insert(i)

for j in l2:
    source2.insert(j)

print("source 1 : ")
for x in source1:
    print(x)
print()

print("source 2: ")
for y in source2:
    print(y)

print()


print()


answer = queue_combine(source1, source2)


print("answer")

for i in answer:
    print(f"{i}")


# Constants
