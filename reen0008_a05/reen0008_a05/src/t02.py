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
from Sorted_List_array import Sorted_List
from Movie_utilities import read_movies

# Movies Data! :)
fh = open('movies.txt', 'r', encoding="utf-8")
movies = read_movies(fh)

# Lists
source1 = Sorted_List()
source2 = Sorted_List()
target, target2, target3, target4, target5, target6 = Sorted_List(
), Sorted_List(), Sorted_List(), Sorted_List(), Sorted_List(), Sorted_List()


source1.insert(movies[0])
source1.insert(movies[0])
print("Clean")
source1.clean()
for i in source1:
    print(i)
    print()

for i in source2:
    print(i)
print()
print()
print("count")
source2.insert(movies[0])
source2.insert(movies[0])
key = movies[0]
n = source2.count(key)
print(n)
print()

key = movies[2]
source2.insert(movies[2])
source2.insert(movies[3])

answer = source2.find(key)


print("find")
print()
print(f"{answer}")
print()

target2.intersection(source1, source2)
print("intersection")
print()

for i in target2:
    print(i)

source2.insert(movies[5])
source2.insert(movies[6])
print()
key = movies[0]
source2.remove_many(key)
print("remove many")
print()
for i in source2:
    print(i)
    print()

target3, target4 = source2.split_alt()
print()
print("split alt")
print()
print("first list")
for i in target3:

    print(i)
    print()
print("second list")
for j in target4:
    print(j)
    print()

target.insert(movies[8])
target.insert(movies[9])

target4.insert(movies[19])
target4.insert(movies[20])
target4.insert(movies[14])
print()
print("union")
print()
target.union(target4, source2)

for j in target:
    print(j)
    print()
key = movies[14]
print()
print()
target5, target6 = target.split_key(key)
print("Split Key")
print()
print("first list")
for j in target5:
    print(j)
    print()

print("second list")
for j in target6:
    print(j)
    print()


# Constants
