# get range of x
from typing import List
from math import sqrt

from . import central_tendencies


def get_range(x: List) -> float:
    return max(x) - min(x)


def get_variance(x: List) -> float:
    """ return variance for the list x """
    return central_tendencies.mean([(i - central_tendencies.mean(x)) ** 2 for i in x])


def get_standard_dev(x: List) -> float:
    """ Get square root of variance """
    return sqrt(get_variance(x))


def get_interquart_range(x: List) -> float:
    return central_tendencies.quantile(0.75, x) - central_tendencies.quantile(0.25, x)


assert get_range([0, 10]) == 10
assert get_variance(list(range(0, 10))) == 8.25
