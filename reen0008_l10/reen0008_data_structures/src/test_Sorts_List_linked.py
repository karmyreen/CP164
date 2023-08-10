"""
-------------------------------------------------------
CP164 
-------------------------------------------------------
Author:  Gurkarman Reen
ID:      169030008
Email:   reen0008@mylaurier.ca
__updated__ = "2023-03-31"
-------------------------------------------------------
"""

# Imports
import random

from List_linked import List
from Number import Number
from Sorts_List_linked import Sorts

# Constants
SIZE = 100  # Size of array to sort.
XRANGE = 1000  # Range of values in random arrays to sort.
TESTS = 100  # Number of random arrays to generate.

SORTS = (
    ('Bubble Sort', Sorts.bubble_sort),
    ('Insertion Sort', Sorts.insertion_sort),
    ('Merge Sort', Sorts.merge_sort),
    ('Quick Sort', Sorts.quick_sort),
    ('Selection Sort', Sorts.selection_sort),
)


def create_sorted():
    """
    -------------------------------------------------------
    Creates a sorted List of Number objects.
    Use: values = create_sorted()
    -------------------------------------------------------
    Returns:
        values - a sorted list of SIZE Number objects (List of Number)
    -------------------------------------------------------
    """

    # your code here
    values = List()

    for i in range(SIZE):
        values.append(Number(i))

    return values


def create_reversed():
    """
    -------------------------------------------------------
    Create a reversed List of Number objects.
    Use: values = create_reversed()
    -------------------------------------------------------
    Returns:
        values - a reversed list of SIZE Number objects (List of Number)
    -------------------------------------------------------
    """

    # your code here
    values = List()
    for i in range(SIZE-1, -1, -1):
        values.append(Number(i))

    return values


def create_randoms():
    """
    -------------------------------------------------------
    Create a 2D list of Number objects with TESTS rows and
    SIZE columns of values between 0 and XRANGE.
    Use: lists = create_randoms()
    -------------------------------------------------------
    Returns:
        lists - TESTS lists of SIZE Number objects containing
            values between 0 and XRANGE (list of List of Number)
    -------------------------------------------------------
    """

    # your code here
    lists = []

    for i in range(TESTS):
        row = List()
        for j in range(SIZE):
            row.append(Number(random.randint(0, XRANGE)))
        lists.append(row)

    return lists


def test_sort(title, func):
    """
    -------------------------------------------------------
    Tests a sort function with Number data and prints the number 
    of comparisons necessary to sort an array:
    in order, in reverse order, and a list of Lists in random order.
    Use: test_sort(title, func)
    -------------------------------------------------------
    Parameters:
        title - name of the sorting function to call (str)
        func - the actual sorting function to call (function)
    Returns:
        None
    -------------------------------------------------------
    """

    # your code here
    Sorts.swaps = 0
    Number.comparisons = 0
    check = create_sorted()

    print("{}".format(title), end='')

    func(check)
    comparisons = Number.comparisons
    swap1 = Sorts.swaps

    Sorts.swaps = 0
    Number.comparisons = 0

    # Reversed List

    check3 = create_reversed()
    func(check3)
    comps = Number.comparisons
    swap2 = Sorts.swaps

    Sorts.swaps = 0
    Number.comparisons = 0

    check2 = create_randoms()
    total = 0

    for i in check2:
        func(i)
        total += Number.comparisons

    avguno = total / len(check2)
    avgdos = Sorts.swaps / len(check2)
    Sorts.swaps = 0

    # Final Table

    print("\t{:>7.0s} {:>7.0f} {:>8.0f} {:>8.0f}\t{:>2.0f} {:>8.0f} {:>8.0f}".format(title,
                                                                                     comparisons, comps, avguno, swap1, swap2, avgdos))
    return
