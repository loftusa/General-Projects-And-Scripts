#%%
import math
import matplotlib.pyplot as plt
import random

#%%
def uniform_pdf(x: int):
    """ Return density function for uniform distribution """
    return 1 if x >= 0 and x < 1 else 0


def uniform_cdf(x: int):
    """ Return probability that a uniform random variable is <= x """
    if x < 0:
        return 0
    elif x > 1:
        return 1
    else:
        return x


def normal_pdf(x, mu=0, sigma=1):
    """ defines a normal distribution. f(x | mu, sigma) = (1/(sqrt(2*pi))*sigma) """
    sqrt_two_pi = math.sqrt(2 * math.pi)
    if sigma != 0:
        return math.exp(-(x - mu) ** 2 / 2 / sigma ** 2) / (sqrt_two_pi * sigma)
    else:
        return None


def normal_cdf(x, mu=0, sigma=1):
    """ Return values for the cdf of the normal distribution """
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2


def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001):
    """find approximate inverse using binary search"""

    # if not standard, compute standard and rescale
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)

    low_z, low_p = -10.0, 0  # normal_cdf(-10) is (very close to) 0
    hi_z, hi_p = 10.0, 1  # normal_cdf(10)  is (very close to) 1
    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2  # consider the midpoint
        mid_p = normal_cdf(mid_z)  # and the cdf's value there
        if mid_p < p:
            # midpoint is still too low, search above it
            low_z, low_p = mid_z, mid_p
        elif mid_p > p:
            # midpoint is still too high, search below it
            hi_z, hi_p = mid_z, mid_p
        else:
            break

    return mid_z


def bernouli_trial(p):
    """ return the result of a single bernouli trial with probability p """
    if random.random() < p:
        return 1
    else:
        return 0


def binomial_pdf(n, p):
    """ return pdf of the binomial distribution """
    return sum(bernouli_trial(p) for _ in range(n))


def checkthing(p):
    return p * (1 - p)
