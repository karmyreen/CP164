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
from functions import matrix_stats 

small, large, total , average = matrix_stats([[2, 10, -1, 1-5], [0, -21, -3, -9], [-10, -10, 9, -11]])

print(f"({small}, {large}, {total}, {average})")