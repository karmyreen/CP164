"""
-------------------------------------------------------
CP164 
-------------------------------------------------------
Author:  Gurkarman Reen
ID:      169030008
Email:   reen0008@mylaurier.ca
__updated__ = "2023-01-22"
-------------------------------------------------------
"""
# Imports


# Constants


def clean_list(values):
    """
    -------------------------------------------------------
    Removes all duplicate values from a list: values contains
    only one copy of each of its integers. The order of values
    must be preserved.
    Use: clean_list(values)
    -------------------------------------------------------
    Parameters:
        values - a list of integers (list of int)
    Returns:
        None
    -------------------------------------------------------
    """

    new_values = []
    for i in values:
        if i not in new_values:
            new_values.append(i)

    print(new_values)

    return


def file_analyze(fv):
    """
    -------------------------------------------------------
    Analyzes the characters in a file.
    The contents of the file must be unchanged.
    Use: u, l, d, w, r = file_analyze(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file reference (file variable)
    Returns:
        u - the number of uppercase letters in the file (int)
        l - the number of lowercase letters in the file (int)
        d - the number of digits in the file (int)
        w - the number of whitespace characters in the file (int)
        r - the number of remaining characters in the file (int)
    -------------------------------------------------------
    """
    u = 0
    l = 0
    d = 0
    w = 0
    r = 0

    line = fv.readline()
    while line != "":
        for i in line:
            if i.isupper():
                u += 1
            elif i.islower():
                l += 1
            elif i.isdigit():
                d += 1
            elif i.isspace():
                w += 1
            else:
                r += 1
        line = fv.readline()
    return u, l, d, w, r


def find_subs(string, sub):
    """
    -------------------------------------------------------
    Finds the indices of the locations of sub within string,
        left to right.
    Use: locations = find_subs(string, sub)
    -------------------------------------------------------
    Parameters:
        string - a string to evaluate (str)
        sub - a substring to locate in string (str)
    Returns:
        locations - an ordered list of the indices of the locations
            of sub within string (list of int)
    -------------------------------------------------------
    """
    location = []

    index = string.find(sub)
    location.append(index)

    while index != -1:
        index = string.find(sub, index + 1)
        location.append(index)

    return location[:-1]


def is_leap_year(year):
    """
    -------------------------------------------------------
    Leap year determination.
    Use: leap_year = is_leap_year(year)
    -------------------------------------------------------
    Parameters:
        year - year to determine if it is a leap year (int > 0)
    Returns:
        leap_year - True if year is a leap year, False otherwise (boolean)
    -------------------------------------------------------
    """
    leap_year = True

    if year % 4 != 0:
        leap_year = False
    elif year % 100 == 0:
        leap_year = False

        if year % 400 == 0:
            leap_year = True

    return leap_year


def is_valid(name):
    """
    -------------------------------------------------------
    Determines if name is a valid Python variable name.
    Variables names must start with a letter or an underscore.
    The rest of the variable name may consist of letters, numbers
    and underscores.
    Use: valid = is_valid(name)
    -------------------------------------------------------
    Parameters:
        name - a string to test as a Python variable name (str)
    Returns:
        valid - True if name is a valid Python variable name,
            False otherwise (boolean)
    -------------------------------------------------------
    """

    valid = False

    if name[0].isalpha() or name[0] == '_':
        valid = True
        for i in name:
            if i.isspace():
                valid = False
            else:
                valid = valid
    return valid


'''
 valid = False

    if name[0].isalpha() or not name[0].isdigit() or not name[0].isspace():

        for i in name[1:]:
            if i.isalpha() or i.isdigit() or not i.isspace():
                valid = True
            else:
                valid = valid
    else:
        valid = valid

    return valid
    
      if name[0].isdigit() or name[0].isspace():
        valid = False
        for i in name:
            if i.isspace():
                valid = False
            else:
                valid = valid
'''


def matrix_transpose(a):
    """
    -------------------------------------------------------
    Transpose the contents of matrix a.
    Use: b = matrix_transpose(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list (list of lists of ?)
    Returns:
        b - the transposed matrix (list of lists of ?)
    -------------------------------------------------------
    """
    b = []
    rows = len(a[0])
    col = len(a)

    for i in range(rows):
        new_mat = []
        for j in range(col):
            new_mat.append(a[j][i])
        b.append(new_mat)

    return b


def matrixes_multiply(a, b):
    """
    -------------------------------------------------------
    Multiplies the contents of matrixes a and b.
    If a is mxn in size, and b is nxp in size, then c is mxp.
    a and b must be unchanged.
    Use: c = matrixes_multiply(a, b)
    -------------------------------------------------------
    Parameters:
        a - a 2D list (2D list of int/float)
        b - a 2D list (2D list of int/float)
    Returns:
        c - the matrix multiple of a and b (2D list of int/float)
    -------------------------------------------------------
    """
    row_a = len(a)
    row_b = len(b)
    col_b = len(b[0])

    # makes empty matrix
    c = [[0] * col_b for x in range(row_a)]

    for i in range(row_a):
        for j in range(col_b):
            for k in range(row_b):
                c[i][j] += a[i][k] * b[k][j]

    return c


def pig_latin(word):
    """
    -------------------------------------------------------
    Converts a word to Pig Latin. The conversion is:
    - if a word begins with a vowel, add "way" to the end of the word.
    - if the word begins with consonants, move the leading consonants to
    the end of the word and add "ay" to the end of that.
    "y" is treated as a consonant if it is the first character in the word,
    and as a vowel for anywhere else in the word.
    Preserve the case of the word - i.e. if the first character of word
    is upper-case, then the new first character should also be upper case.
    Use: pl = pig_latin(word)
    -------------------------------------------------------
    Parameters:
        word - a string to convert to Pig Latin (str)
    Returns:
        pl - the Pig Latin version of word (str)
    ------------------------------------------------------
    """
    word = str(word)
    pl = ''
    vowels = ['a', 'i', 'o', 'e', 'u']
    for i in vowels:
        if word.startswith(i):
            pl = word + "way"

        else:
            pl = word[1:] + word[0] + "ay"

    return pl


def shift(string, n):
    """
    -------------------------------------------------------
    Encipher a string using a shift cipher.
    Only letters are enciphered, and the returned string is
    in upper case.
    Use: estring = shift(string, n):
    -------------------------------------------------------
    Parameters:
        string - string to encipher (str)
        n - the number of letters to shift (int)
    Returns:
        estring - the enciphered string (str)
    -------------------------------------------------------
    """

    estring = ''

    for i in string.lower():
        shift = ord(i) + (n % 26)
        if shift >= 123:
            shift -= 26

        estring += chr(shift).upper()

    return estring
