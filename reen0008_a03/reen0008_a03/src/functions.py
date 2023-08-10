"""
-------------------------------------------------------
CP164 
-------------------------------------------------------
Author:  Gurkarman Reen
ID:      169030008
Email:   reen0008@mylaurier.ca
__updated__ = "2023-02-06"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from enum import Enum

# Enumerated constant
MIRRORED = Enum('MIRRORED',
                {'IS_MIRRORED': "is a mirror", 'TOO_MANY_LEFT': "too many characters in L",
                 'TOO_MANY_RIGHT': "too many characters in R", 'MISMATCHED': "L and R don't match",
                 'INVALID_CHAR': "invalid character", 'NOT_MIRRORED': "no mirror character"})

OPERATORS = "+-*/"


def stack_split_alt(source):
    """
    -------------------------------------------------------
    Splits the source stack into separate target stacks.
    When finished source stack is empty. Values are
    pushed alternately onto the returned target stacks.
    Use: target1, target2 = stack_split_alt(source)
    -------------------------------------------------------
    Parameters:
        source - the stack to split into two parts (Stack)
    Returns:
        target1 - contains alternating values from source (Stack)
        target2 - contains other alternating values from source (Stack)
    -------------------------------------------------------
    """
    target1 = Stack()
    target2 = Stack()
    i = 0

    while not source.is_empty():

        if i % 2 == 0:
            target1.push(source.pop())
        else:
            target2.push(source.pop())
        i += 1

    return target1, target2


def is_palindrome_stack(string):
    """
    -------------------------------------------------------
    Determines if string is a palindrome. Ignores case, digits, spaces, and
    punctuation in string.
    Use: palindrome = is_palindrome_stack(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if string is a palindrome, False otherwise (bool)
    -------------------------------------------------------
    """
    palindrome = False

    stack = Stack()

    for i in string:
        stack.push(i)

    reverse = ""

    while not stack.is_empty():
        reverse = reverse + stack.pop()

    if reverse == string:
        palindrome = True
    else:
        palindrome = palindrome
    return palindrome


def postfix(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = postfix(string)
    -------------------------------------------------------
    Parameters:
        string - the postfix string to evaluate (str)
    Returns:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """
    stack = Stack()

    string = string.split()
    for i in string:

        if i.isdigit():
            stack.push(int(i))

        elif i in OPERATORS:
            num1 = stack.pop()
            num2 = stack.pop()
            if i == "+":
                stack.push(num2+num1)
            elif i == "-":
                stack.push(num2-num1)
            elif i == "/":
                stack.push(num2/num1)
            elif i == "*":
                stack.push(num2*num1)

    answer = float(stack.pop())

    return answer


def stack_maze(maze):
    """
    -------------------------------------------------------
    Solves a maze using Depth-First search.
    Use: path = stack_maze(maze)
    -------------------------------------------------------
    Parameters:
        maze - dictionary of points in a maze, where each point
            represents a corridor end or a branch. Dictionary
            keys are the name of the point followed by a list of
            branches, if any. First point is named 'Start', exit
            is named 'X' (dict)
    Returns:
        path - list of points visited before the exit is reached,
            None if there is no exit (list of str)
    -------------------------------------------------------
    """
    stack = Stack()
    path = []
    key = "Start"
    valid = True

    while not "X" in path and valid:
        for i in maze[key]:
            if not i in path:
                stack.push(i)
        if stack.is_empty():
            valid = False
        else:
            key = stack.pop()
            path.append(key)
    if "X" not in path:
        path = None

    return path


def is_mirror_stack(string, valid_chars, m):
    """
    -------------------------------------------------------
    Determines if string is a mirror of characters in valid_chars around the pivot m.
    A mirror is of the form LmR, where L is the reverse of R, and L and R
    contain only characters in valid_chars.
    Use: mirror = is_mirror_stack(string, valid_chars, m)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
        valid_chars - a string of valid characters (str)
        m - the mirror pivot string (str - one character not in valid_chars)
    Returns:
        mirror - the state of the string (Enum MIRRORED)
    -------------------------------------------------------
    """
    assert m not in valid_chars, \
        f"cannot use '{m}' as the mirror character"

    mirror = MIRRORED.IS_MIRRORED
    stack = Stack()
    n = len(string)
    i = 0
    left = 0
    right = 0
    valid_mirror = True

    if m not in string:
        valid_mirror = False
        mirror = MIRRORED.NOT_MIRRORED

    while i < n and string[i] != m and valid_mirror:
        if string[i] in valid_chars:
            stack.push(string[i])
            i += 1
            left += 1
        else:
            valid_mirror = False
            mirror = MIRRORED.INVALID_CHAR

    # skip over the mirror character
    i += 1

    while mirror and i < n and not stack.is_empty() and valid_mirror:
        c = stack.pop()

        if string[i] != c:
            valid_mirror = False
            mirror = MIRRORED.MISMATCHED
        else:
            i += 1
            right += 1

    # check final conditions
    if not (i == n and stack.is_empty()) and valid_mirror:
        if left > right:
            valid_mirror = False
            mirror = MIRRORED.TOO_MANY_LEFT
        else:
            mirror = MIRRORED.TOO_MANY_RIGHT

        '''if right > left:
            valid_mirror = False
            mirror = MIRRORED.TOO_MANY_RIGHT
        '''

    return mirror
