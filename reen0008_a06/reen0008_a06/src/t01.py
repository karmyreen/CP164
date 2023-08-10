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

from Queue_linked import Queue

q1 = Queue()
q2 = Queue()
q3 = Queue()


q1.insert(5)
q1.insert(6)
q1.insert(8)
q1.insert(8)
q1.insert(10)

q2.insert(1)
q2.insert(2)
q2.insert(3)

q3.insert(7)
q3.insert(2)
q3.insert(0)


empty = q1.is_empty()

print(empty)

print()
remove = q1.remove()

for i in q1:
    print(i)
    print()
peek = q1.peek()
print()
print(peek)

print()
q1._append_queue(q2)

for i in q1:
    print(i)
    print()
print()

q3.combine(q1, q2)

for i in q3:
    print(i)
    print()
print(0)

split1, split2 = q3.split_alt()
print()
print("first list")
for i in split1:
    print(i)
    print()
print()
print("second list")
for j in split2:
    print(j)
    print()

equals = q1 == q3

print(equals)


# Constants
