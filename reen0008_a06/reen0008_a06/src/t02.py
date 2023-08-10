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
from Priority_Queue_linked import Priority_Queue

pq1 = Priority_Queue()
pq2 = Priority_Queue()
pq3 = Priority_Queue()
pq4 = Priority_Queue()
pq5 = Priority_Queue()

pq1.insert(1)
pq1.insert(4)
pq1.insert(9)
pq1.insert(2)
pq1.insert(10)


pq2.insert(2)
pq2.insert(9)
pq2.insert(3)
pq2.insert(10)
pq2.insert(4)


pq3.insert(3)
pq3.insert(1)
pq3.insert(10)
pq3.insert(4)
pq3.insert(8)

pq4.insert(8)
pq4.insert(1)
pq4.insert(11)
pq4.insert(3)

pq5.insert(8)
pq5.insert(1)
pq5.insert(11)


empty = pq1.is_empty()

print(empty)


remove = pq2.remove()

print("removed")
print(remove)
print()

for i in pq2:
    print(i)
    print()
print()

v = pq3.peek()

print(v)

print()

target1, target2 = pq1.split_alt()

print("first list")
for i in target1:
    print(i)
    print()
print()
print("second list")
for j in target2:
    print(j)
    print()
print()

target11, target22 = pq3.split_key(4)
print("first list")
for i in target11:
    print(i)
    print()
print()
print("second list")
for j in target22:
    print(j)
    print()
print()


pq5.combine(pq5, pq4)

for i in pq5:
    print(i)
    print()
print()


pq5._append_queue(pq4)

for i in pq5:
    print(i)
    print()
print()

# Constants
