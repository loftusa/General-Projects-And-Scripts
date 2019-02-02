from typing import List, Union, Iterable
from collections import Counter
import sys

from linalg import vectors

# Define the mean
def mean(x: List) -> float:
    return sum(x) / len(x)


# Define the median
def median(x: List) -> float:
    x = sorted(x)  # sort in ascending order
    mid = len(x) // 2

    if len(x) % 2 == 0:
        return mean([x[mid], x[mid - 1]])  # return mean of the middle two numbers
    else:
        return x[mid]


# Define a function to get the mode
def mode(x: List) -> List:
    c = Counter(x)
    max_count = max(c.values())
    return [x_i for x_i, count in c.items() if count == max_count]


# Define a function to get the pth quantile
def quantile(p: float, x: List) -> float:
    """ Return p-th percentile value in x """
    x = sorted(x)
    p_index = int(p * len(x))
    return x[p_index]


# Define a function to get range
def data_range(x: List) -> Union[float, int]:
    """ Return the range of x """
    return max(x) - min(x)


def de_mean(x: List) -> Iterable:
    """ Subtract the mean from all elements of x """
    return map(lambda i: i - mean(x), x)  # Use map function for practice


def variance(x: List) -> float:
    """ Assumes x has at least two elements. Compute variance of x. """
    n = len(x)
    dmn = de_mean(x)
    deviations = vectors.sum_of_squares(dmn) / n


x = [1, 2, 3, 4, 5]

assert mean(x) == 3
assert median(x) == 3
assert median([1, 2, 3, 4, 5, 6]) == 3.5
assert quantile(0.5, x) == 3
assert data_range(x) == 4
assert list(de_mean(x)) == [1 - 3, 2 - 3, 3 - 3, 4 - 3, 5 - 3]
