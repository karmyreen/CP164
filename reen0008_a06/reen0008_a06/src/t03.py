"""
-------------------------------------------------------
CP164 
-------------------------------------------------------
Author:  Gurkarman Reen
ID:      169030008
Email:   reen0008@mylaurier.ca
__updated__ = "2023-03-12"
-------------------------------------------------------
"""
# Imports

from Deque_linked import Deque

dq = Deque()
dq2 = Deque()
dq3 = Deque()

dq.insert_rear(1)
dq.insert_rear(5)
dq.insert_rear(9)
dq.insert_rear(2)

dq2.insert_rear(1)
dq2.insert_rear(0)
dq2.insert_rear(10)
dq2.insert_front(5)

dq3.insert_rear(1)
dq3.insert_rear(9)
dq3.insert_rear(10)
dq3.insert_front(3)

v = dq3.remove_rear()
print("removed")
print(v)

for i in dq3:
    print(i)
    print()
print()

fv = dq2.remove_front()
print("removed")
print(fv)
for i in dq2:
    print(i)
    print()
print()


v = dq.peek_front()
print(v)
print()

v = dq.peek_rear()
print(v)

l = dq._front._next  # l is second node from the front
r = dq._rear._prev
print()
dq._swap(l, r)
print("swap:")
print()
for i in dq:
    print(i)
    print()
print()


# Constants
