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
from functions import generate_matrix_num, print_matrix_num

rows = int(input("# of rows: "))
cols = int(input("# of columns : "))
low = int(input("Minimum value for range: "))
high = int(input("Maximum value for range: "))
type_v = str(input("Int or float values: "))

matrix = generate_matrix_num(rows,cols,low,high,type_v)

print_matrix_num(matrix, type_v)


