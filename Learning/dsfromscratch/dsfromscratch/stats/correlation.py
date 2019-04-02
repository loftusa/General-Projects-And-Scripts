""" 
Functions to describe correlation -- e.g., get_covariance.
Scenario: list `daily_minutes`, minutes per day each user spends on company.
          list `num_friends`, 
"""
#%%
import sys

from .centraltendencies import mean
from ..linalg.vectors import dot
from .dispersion import get_standard_dev, get_variance
from typing import List
import numpy as np
import matplotlib.pyplot as plt


def get_covariance(x: List, y: List) -> float:
    """ Return the covariance of x and y. 
    Covariance(X, Y) = E[(X - E[X])(Y - E[y])] """
    return dot([i - mean(x) for i in x], [j - mean(y) for j in y]) / (len(x) - 1)


def get_correlation(x: List, y: List) -> float:
    """ return correlation of x and y. 
    -1: one is the reverse of the other
    0: no  
    1: they're the same """
    std_x = get_standard_dev(x)
    std_y = get_standard_dev(y)
    if std_x > 0 and std_y > 0:
        return get_covariance(x, y) / (std_x * std_y)
    else:
        return 0


#%%

