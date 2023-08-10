"""
-------------------------------------------------------
CP164 
-------------------------------------------------------
Author:  Gurkarman Reen
ID:      169030008
Email:   reen0008@mylaurier.ca
__updated__ = "2023-02-20"
-------------------------------------------------------
"""
# Imports
from List_array import List
from Movie_utilities import read_movies

# Movies Data! :)
fh = open('movies.txt', 'r', encoding="utf-8")
movies = read_movies(fh)

# Lists
source1, source2 = List(), List()
target, target2 = List(), List()

# Append Task
print("Append Task: ")
target.append(movies[0])
for i in target:
    print(i)
print()


# Clean Task
target.clean()
print("Clean Task: ")
for i in target:
    print(i)
print()

# Combine Task
source1.append(movies[1])
source2.append(movies[2])
target.combine(source1, source2)
print("Combine Task: ")
for i in target:
    print(i)
print()


# Intersection Task
target.intersection(source1, source2)
print("Intersection Task: ")
for i in target:
    print(i)
print()

# Remove_Front Task
value = target.remove_front()
print(f"Remove_Front Task- Value removed: {value}")
print()

# Remove_Many Task
key = 55
source1.remove_many(key)
print(f"Remove_Front Task- Values remaining: {source1._values}")
print()

# Split Task
answer, answer2 = target.split()
print("Split Task: ")
print("Source 1: ")
for i in answer:
    print(i)
print("Source 2: ")
for k in answer2:
    print(k)
print()

# Split_Alt Task
print("Split_Alt")
target.append(movies[1]), target.append(
    movies[2]), target.append(movies[3]), target.append(movies[4])
answer, answer2 = target.split_alt()
print("Target 1: ")
for i in answer:
    print(i)
print("Target 2:")
for i in answer2:
    print(i)
print()

# Union Task
source1.append(movies[7])
source2.append(movies[5])
target.union(source1, source2)
print("Union Task: ")
for i in target:
    print(i)
print()
