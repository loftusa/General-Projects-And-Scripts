""" defines function for performing hypothesis testing. """
from . import densityfunctions
from .densityfunctions import normal_cdf, inverse_normal_cdf
import math

# flip a coin some number n times and count the number of heads X
# each coin flip is a Bernoulli trial, so X is a binomial (n, p) random variable
# Given an outcome, what is P(p = 0.5?)
def normal_approximation_to_binomial(n, p):
    """ finds mu and sigma corresponding to a Binomial(n,p) """
    mu = p * n
    sigma = math.sqrt(p * (1 - p) * n)  # not sure why this is true
    return mu, sigma


# given a random variable follows a normal distribution,
# Define functions for figuring out the probability that the realized values of a function lie within (or outside) a particular interval
def normal_probability_above(lo, mu=0, sigma=1):
    """ Get probability that the r.v. will be above `lo` """
    return 1 - normal_cdf(lo, mu=mu, sigma=sigma)


def normal_probability_between(lo, hi, mu=0, sigma=1):
    """ get probability that the r.v. will be between `lo` and `hi` """
    prob_hi = normal_cdf(hi, mu=mu, sigma=sigma)
    prob_low = normal_cdf(lo, mu=mu, sigma=sigma)
    return prob_hi - prob_low


def normal_probability_outside(lo, hi, mu=0, sigma=1):
    """ get probability that the r.v. will not be between `lo` and `hi` """
    return 1 - normal_probability_between(lo, hi, mu=mu, sigma=sigma)


# given a random variable that follows a normal distribution,
# find intervals that satisfy the given probability
def normal_upper_bound(p, mu=0, sigma=1):
    """ return the z for which P(Z <= z) = p """
    return inverse_normal_cdf(1 - p, mu=mu, sigma=sigma)


def normal_lower_bound(p, mu=0, sigma=1):
    """ return the z for which P(Z >= z) = p """
    return inverse_normal_cdf(p, mu=mu, sigma=sigma)


def normal_two_sided_bounds(p, mu=0, sigma=1):
    """ return the symmetric (about the mean) bounds """
    tail = (1 - p) / 2
    lower = normal_lower_bound(tail, mu=mu, sigma=sigma)
    upper = normal_upper_bound(tail, mu=mu, sigma=sigma)
    return lower, upper


def two_sided_p_value(x, mu=0, sigma=1):
    """
    Compute probability that we would see a value at least as extreme as the one observed 
    """
    if x >= mu:
        # if x is greater than the mean, the tail is what's greater than x
        return 2 * normal_probability_above(x, mu, sigma)
    else:
        # if x is less than the mean, the tail is what's less than x
        return 2 * normal_cdf(x, mu, sigma)

