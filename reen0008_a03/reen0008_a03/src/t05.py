"""
-------------------------------------------------------
CP164 
-------------------------------------------------------
Author:  Gurkarman Reen
ID:      169030008
Email:   reen0008@mylaurier.ca
__updated__ = "2023-02-05"
-------------------------------------------------------
"""
# Imports
from functions import stack_maze

'''maze = maze = {'Start': ['A'], 'A': ['B', 'C'], 'B': [], 'C': ['D', 'E'],
               'D': [], 'E': ['F', 'X'], 'F': ['G', 'H'], 'G': [], 'H': []}
'''

'''maze = {'Start': ['A'], 'A': ['B', 'C'], 'B': [], 'C': ['D', 'E'],
        'D': [], 'E': ['X', 'F'], 'F': ['G'], 'G': ['C']}
'''

maze = {'Start': ['A'], 'A': []}


answer = stack_maze(maze)

print(answer)


# Constants
