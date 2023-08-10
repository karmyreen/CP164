"""
-------------------------------------------------------
CP164 
-------------------------------------------------------
Author:  Gurkarman Reen
ID:      169030008
Email:   reen0008@mylaurier.ca
__updated__ = "2023-02-17"
-------------------------------------------------------
"""
# Imports

# Constants


def recurse(x, y):
    """
    -------------------------------------------------------
    Recursive function - example of tree recursion.
    Use: ans = recurse(x, y)
    -------------------------------------------------------
    Parameters:
        x - an integer (int)
        y - an integer (int)
    Returns:
        ans - the function result (int)
    -------------------------------------------------------
    """

    if x < 0 or y < 0:
        ans = x - y
    else:
        ans = (recurse(x-1, y)) + (recurse(x, y-1))
    return ans


def gcd(m, n):
    """
    -------------------------------------------------------
    Recursively find the Greatest Common Denominator of two numbers.
    Use: ans = gcd(m, n)
    -------------------------------------------------------
    Parameters:
        n - an integer (int)
        m - an integer (int)
    Returns:
        ans - the function result (int)
    -------------------------------------------------------
    """

    if m % n == 0:
        ans = n
    else:
        ans = gcd(m, m % n)
    return ans


def vowel_count(s):
    """
    -------------------------------------------------------
    Recursively counts number of vowels in a string.
    Use: count = vowel_count(s)
    -------------------------------------------------------
    Parameters:
        s - string to examine (str)
    Returns:
        count - number of vowels in s (int)
    -------------------------------------------------------
    """
    vowels = "aeiou"
    count = 0

    if s == "":
        count = count
    elif s[0].lower() in vowels:

        count = 1 + vowel_count(s[1:])

    else:
        count = vowel_count(s[1:])

    return count


def to_power(base, power):
    """
    -------------------------------------------------------
    Calculates base^power.
    Use: ans = to_power(base, power)
    -------------------------------------------------------
    Parameters:
        base - base to apply power to (float)
        power - power to apply (int)
    Returns:
        ans - base ^ power (float)
    -------------------------------------------------------
    """

    if power == 0:
        ans = 1
    else:
        if power < 0:
            ans = 1 / to_power(base, -power)
        else:
            ans = base * to_power(base, power - 1)

    return ans


def is_palindrome(s):
    """
    -------------------------------------------------------
    Recursively determines if s is a palindrome. Ignores non-letters and case.
    Use: palindrome = is_palindrome(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        palindrome - True if s is a palindrome, False otherwise (boolean)
    -------------------------------------------------------
    """

    if s == "":
        palindrome = True
    elif not s[0].isalpha():
        palindrome = is_palindrome(s[1:])
    elif not s[-1].isalpha():
        palindrome = is_palindrome(s[:-1])
    else:
        if s[0].lower() == s[-1].lower():
            palindrome = is_palindrome(s[1:-1])

        else:
            palindrome = False

    return palindrome


def bag_to_set(bag):
    """
    -------------------------------------------------------
    Copies elements of a bag to a set.
    Use: new_set = bag_to_set(bag)
    -------------------------------------------------------
    Parameters:
        bag - a list of values (list)
    Returns:
        new_set - containing one each of the elements in bag (list)
    -------------------------------------------------------
    """

    new_set = []

    bag_to_set_aux(bag, new_set)

    return new_set


def bag_to_set_aux(bag, new_set):

    if bag == []:
        return
    else:
        if bag[0] not in new_set:
            new_set.append(bag[0])

    return bag_to_set_aux(bag[1:], new_set)
