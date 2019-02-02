""" 
This module defines functions for creating and operating on matrices
(defined as lists of lists) 
"""

from vectors import *

def get_row(A: List[List], i: int) -> List:
    return A[i]


def get_column(A: List[List], j: int) -> List:
    return [i[j] for i in A]

def shape(A: List[List]) -> tuple:
    num_rows = len(A)
    num_cols = len(A) if A else 0
    return (num_rows, num_cols)

def make_matrix(num_rows: int, num_cols: int, entry_fn: 'function') -> List[List]:
    """ Return num_rows x num_cols matrix A where A[i, j] 
    is the result of calling function(i, j) """
    return [[entry_fn(i, j) for j in range(num_cols)] for i in range(num_rows)]

def is_diagonal(i: int, j: int) -> int:
    """ 1 if i == j, else 0 """
    return 1 if i == j else 0

assert get_row(vec, 0) == [1, 2, 3]
assert get_column(vec, 0) == [1, 4, 7]
assert shape(vec) == (3, 3)

# Make a matrix A
A = make_matrix(3, 3, is_diagonal)
for s in A:
    print(s)
print('\n')

friendships = [
[0, 1, 1, 0, 0, 0, 0, 0, 0, 0], # user 0
[1, 0, 1, 1, 0, 0, 0, 0, 0, 0], # user 1
[1, 1, 0, 1, 0, 0, 0, 0, 0, 0], # user 2
[0, 1, 1, 0, 1, 0, 0, 0, 0, 0], # user 3
[0, 0, 0, 1, 0, 1, 0, 0, 0, 0], # user 4
[0, 0, 0, 0, 1, 0, 1, 1, 0, 0], # user 5
[0, 0, 0, 0, 0, 1, 0, 0, 1, 0], # user 6
[0, 0, 0, 0, 0, 1, 0, 0, 1, 0], # user 7
[0, 0, 0, 0, 0, 0, 1, 1, 0, 1], # user 8
[0, 0, 0, 0, 0, 0, 0, 0, 1, 0]  # user 9
]

# Find the number of connections each node in `friendships` has
from collections import Counter

connections = {i: sum(j) for i, j in enumerate(friendships)}
print(connections, '\n')

friends_of_five = [i for i, is_friend in enumerate(friendships[5]) if is_friend]
print(friends_of_five, '\n')  # Print the friends of five

