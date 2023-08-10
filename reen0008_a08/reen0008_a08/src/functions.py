"""
-------------------------------------------------------
CP164 
-------------------------------------------------------
Author:  Gurkarman Reen
ID:      169030008
Email:   reen0008@mylaurier.ca
__updated__ = "2023-03-27"
-------------------------------------------------------
"""
# Imports

# Constants
from Letter import Letter


def do_comparisons(file_variable, bst):
    """
    -------------------------------------------------------
    Retrieves every letter in file_variable from bst. Generates
    comparisons in bst objects. Each Letter object in bst contains
    the number of comparisons found by searching for that Letter
    object in file_variable.
    Use: do_comparisons(file_variable, bst)
    -------------------------------------------------------
    Parameters:
        file_variable - the already open file containing data to evaluate (file)
        bst - the binary search tree containing 26 Letter objects
            to retrieve data from (BST)
    Returns:
        None
    -------------------------------------------------------
    """
    # Zeroes out all comparison values in tree nodes
    for node in bst:
        node.comparisons = 0

    # your code here

    for i in file_variable:
        for x in i:
            if x.isalpha():
                bst.retrieve(Letter(x.upper()))
    return


def comparison_total(bst):
    """
    -------------------------------------------------------
    Sums the comparison values of all Letter objects in bst.
    Use: total = comparison_total(bst)
    -------------------------------------------------------
    Parameters:
        bst - a binary search tree of Letter objects (BST)
    Returns:
        total - the total of all comparison fields in the bst
            Letter objects (int)
    -------------------------------------------------------
    """
    list = bst.inorder()
    total = 0
    for x in list:
        total += x.comparisons

    return total


def letter_table(bst):
    """
    -------------------------------------------------------
    Prints a table of letter counts for each Letter object in bst.
    Use: letter_table(bst)
    -------------------------------------------------------
    Parameters:
        bst - a binary search tree of Letter objects (BST)
    Returns:
        None
    -------------------------------------------------------
    """
    val = bst.inorder()
    total = 0

    for i in val:
        total += i.count

    print("Letter Count/Percent Table")
    print()

    print("Total Count: {:,}".format(total))

    print()

    print("Letter  Count       %")

    print("---------------------")
    for j in val:
        check2 = j.count / total * 100
        print("{:>4s}{:>8,d}{:9.2f}%".format(j.letter, j.count, check2))
    return
