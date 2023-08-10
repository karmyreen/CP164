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

from Queue_circular import Queue


l1 = [5, 4, 2, 1, 6, 10]
l2 = [5, 4, 2, 1, 6, 10]


cq = Queue()
cq2 = Queue()


for x in l1:
    cq2.insert(x)
for j in l1:
    cq.insert(j)

equals = cq == cq2

print(equals)


if len(l1) == 0:
    print("not valid")
else:
    i = 5

    print(f"Is it empty: {cq.is_empty()}")
    print(f"insert: {cq.insert(i)}")
    print(f"remove: \n{cq.remove()}")
    print(f"peek:\n{cq.peek()}")


print(cq._values)
