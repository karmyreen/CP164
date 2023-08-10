"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Gurkarman Reen
ID:      169030008
Email:   reen0008@mylaurier.ca
__updated__ = "2022-11-28"
-------------------------------------------------------
"""
# Imports
import random 


def generate_matrix_num(rows, cols, low, high, value_type):
    """
    -------------------------------------------------------
    Generates a 2D list of numbers of the given type, 'float' or 'int'.
    (To generate random float number use random.uniform and to
    generate random integer number use random.randint)
    Use: matrix = generate_matrix_num(rows, cols, low, high, value_type)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the list (int > 0)
        cols - number of columns (int > 0)
        low - low value of range (float)
        high - high value of range (float > low)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        matrix - a 2D list of random numbers (2D list of float/int)
    -------------------------------------------------------
    """
    
    matrix = []
    
    if value_type == "float":
        
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(random.uniform(low,high))
            matrix.append(row )
    elif value_type == "int" :
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(random.randint(low, high))
            matrix.append(row)
            
    return matrix 



def print_matrix_num(matrix, value_type):
    """
    -------------------------------------------------------
    Prints the contents of a 2D list in a formatted table.
    Prints float values with 2 decimal points and prints row and
    column headings.
    Use: print_matrix_num(matrix, 'float')
    Use: print_matrix_num(matrix, 'int')
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of values (2D list)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        None.
    -------------------------------------------------------
    """
    
    
    print(f" ", end = "")
    for w in range(len(matrix[0])):
        print(f"{w:6d}", end = "")
    
    print()
    for i in range(len(matrix)):
        print(f"{i}", end='')
        for j in range(len(matrix[0])):
            
            if value_type == "int":
                print(f" {matrix[i][j]:5d}", end = "")
            if value_type == "float":
                print(f" {matrix[i][j]:5.2f}", end = "")
        if i != len(matrix)-1:
            print()
    
                
            
                
    return 






    
def matrix_stats(matrix):
    """
    -------------------------------------------------------
    Returns statistics on a 2D list.
        Use: smallest, largest, total, average = matrix_stats(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of numbers (2D list of float/int)
    Returns:
        smallest - the smallest number in matrix (float/int)
        largest - the largest number in matrix (float/int)
        total - the total of the numbers in matrix (float/int)
        average - the average of numbers in matrix (float/int)
    -------------------------------------------------------
    """
    if len(matrix) > 0 :
        small = matrix[0][0]
        large = matrix [0][0] 
        
    
    total = 0
    count = 0 
    
    for i in range(len(matrix)): 
        for j in range(len(matrix[0])):
            if small > matrix[i][j]:
                small= matrix[i][j]
            if large < matrix [i][j]:
                large = matrix[i][j]
            total = total + matrix[i][j]
            count = count + 1 
            
    average = total / count 
    smallest = small 
    largest = large 
    
    return smallest, largest, total, average 




def find_less(matrix, n):
    """
    -------------------------------------------------------
    Finds the location [row, column] of the first value in matrix
    that is smaller than a target value, n. If there is no such
    number in matrix, it should return an empty list.
    Use: loc = find_less(matrix, n)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of numbers (2D list)
        n - the target value (float)
    Returns:
        loc - a list of the row and column location of
            the first value smaller than n in values,
            an empty list otherwise (list of int)
    -------------------------------------------------------
    """
    
    loc = []
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
                if matrix[i][j] < n and len(loc) == 0 :
                        loc.append(i)
                        loc.append(j)
                    
                
    return loc 




def matrix_scalar_multiply(matrix, num):
    """
    -------------------------------------------------------
    Update matrix by multiplying each element of matrix by num.
    Use: matrix_scalar_multiply(matrix, num)
    -------------------------------------------------------
    Parameters:
        matrix - the matrix to multiply (2D list of int/float)
        num - the number to multiply by (int/float)
    Returns:
        None
    ------------------------------------------------------
    """
  
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = matrix[i][j]*num 
            
  
    
   
    
    return 
                    
                
                
                
            
   
            
    
   
            
            
        
            
                
                