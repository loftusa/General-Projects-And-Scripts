# TODO: fix type hinting for vector_mean, get_row, get_column

""" This module defines functions for operating on vectors (which, to make things easy, we are defining as just Lists) """

from typing import List

import math

height_weight_age = [70, 170, 40]
grades = [95, 80, 75, 62]


def vector_add(v: List, w: List) -> List:
    """ Add corresponding elements """
    return [sum(i) for i in zip(v, w)]


def vector_subtract(v: List, w: List) -> List:
    """ Subtract corresponding elements """
    return [i[0] - i[1] for i in zip(v, w)]


def vector_sum(vectors: List) -> List:
    """ vectors is a list of vectors"""
    return [sum(i) for i in zip(*vectors)]


def vector_multiply(v: List, scal: int) -> List:
    """ Scalar multiplication for a vector """
    return [i * scal for i in v]


def vector_mean(vectors: List[List]) -> List:
    """ Compute componentwise mean of a set of vectors """
    return [i / len(vectors) for i in vector_sum(vectors)]


def dot(v: List, w: List) -> List:
    """ return sum of componentwise products of v and w """
    return sum([i[0] * i[1] for i in zip(v, w)])


def sum_of_squares(v: List) -> int:
    """ Square each element of a vector then return the sum """
    return dot(v, v)


def magnitude(v: List) -> int:
    """ Return the pythagorean length of v """
    return math.sqrt(sum_of_squares(v))


def squared_distance(v: List, w: List) -> int:
    """(v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2"""
    return sum_of_squares(vector_subtract(v, w))


def distance(v: List, w: List) -> int:
    return math.sqrt(squared_distance(v, w))


vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

assert vector_add(vec[0], vec[1]) == [5, 7, 9]
assert vector_subtract(vec[0], vec[1]) == [-3, -3, -3]
assert vector_sum(vec) == [12, 15, 18]
assert vector_multiply(vec[0], 2) == [2, 4, 6]
assert vector_mean(vec) == vec[1]
assert dot(vec[0], vec[1]) == 32
assert sum_of_squares(vec[0]) == 14
assert magnitude(vec[0]) == math.sqrt(14)
