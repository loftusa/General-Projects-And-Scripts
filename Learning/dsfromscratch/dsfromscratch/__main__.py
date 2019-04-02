#%%
print(f"name of __main__.py: {__name__}")
import sys, os

# for vscode data science tools
#### -----------------------------------------------
toplevel = "/Users/alex/Dropbox/Programming/Jupyter-Notebooks/Learning/dsfromscratch"
if not toplevel in sys.path:
    print(f"inserting toplevel. Path: {sys.path}")
    sys.path.insert(0, toplevel)
else:
    print(f"toplevel already in. Path: {sys.path}")

print(f"dsfromscratch in dir: {'dsfromscratch' in sys.path}")
#### -----------------------------------------------
from importlib import reload

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random
import math
import dsfromscratch

print("dsfromscratch loaded above this in code")
from dsfromscratch.utils import graphing
from dsfromscratch import *
from dsfromscratch._vars import *

#%%
print(f"Global dir: {dir()}")
print(f"probability dir: {dir(probability)}")
plt.scatter(num_friends, daily_minutes)

#%%
# remove that outlier
# num_friends = [i for i in num_friends if i < 80]
# daily_minutes = [i for i in daily_minutes if i > 2]
# plt.scatter(num_friends, daily_minutes)

# #%%
# print(len(num_friends))
# print(len(daily_minutes))


# #%%
# # stats.correlation.get_correlation(num_friends, daily_minutes)
# print(dir(stats))

# #%%
# stats.correlation.get_correlation(num_friends, daily_minutes)

# #%%
# # Simpson's Paradox
# coast = ["west coast", "east coast", "west coast", "east coast"]
# degree = ["PhD", "PhD", "no PhD", "no PhD"]
# num_members = [35, 70, 66, 33]
# nfriends = [3.1, 3.2, 10.9, 13.4]
# df = pd.DataFrame(
#     {"coast": coast, "degree": degree, "num_members": num_members, "nfriends": nfriends}
# )
# df

# #%%
# df.groupby(["coast"]).mean()

# #%%
# df.groupby(["degree"]).mean()

# #%%
# x = [-2, -1, 0, 1, 2]
# y = [2, 1, 0, 1, 2]
# stats.correlation.get_correlation(x, y)

# #%%
# x = [-2, -1, 0, 1, 2]
# y = [99.98, 99.99, 100, 100.01, 100.05]
# print(stats.correlation.get_correlation(x, y))

# #%%
# # --------------------------

# # Check that, if all you know is that at least one of the children is a girl, then it is twice as likely that the family has one boy and one girl than it has both girls

# both_girls = 0
# older_girl = 0
# either_girl = 0

# random.seed(0)

# for _ in range(10000):
#     younger = probability.conditional.random_kid()
#     older = probability.conditional.random_kid()
#     if older == "girl":
#         older_girl += 1
#     if older == "girl" and younger == "girl":
#         both_girls += 1
#     if older == "girl" or younger == "girl":
#         either_girl += 1

# print(both_girls, older_girl, either_girl)

# print("P(both | older:", both_girls / older_girl)
# print("P(either | younger:", both_girls / either_girl)

# #%%
# graphing.gr(probability.densityfunctions.normal_pdf, min=-5, max=5)

# #%%
# print("current: ", dir())
# print("prob: ", dir(probability))
# #%%
# from dsfromscratch.probability import hyptest
# from dsfromscratch.probability import densityfunctions
# print(f"dir right after imports: {dir()}")

# lower, upper = hyptest.normal_two_sided_bounds(1)
# print(lower, upper)

# print(hyptest.normal_two_sided_bounds(0.5))
# print(hyptest.normal_probability_above(0.25))
# print(hyptest.normal_lower_bound(0.25))
# print(hyptest.normal_upper_bound(0.25))
# print(hyptest.normal_lower_bound.__doc__)

# #%%
# from dsfromscratch.probability.densityfunctions import normal_cdf, normal_pdf
# mu_0, sigma_0 = hyptest.normal_approximation_to_binomial(10, 0.5)
# print(mu_0)
# print(sigma_0)
# graphing.gr(normal_pdf, mu=mu_0, sigma=sigma_0, min=3, max=8)

# #%%
# for i in range(1, 6):
#     graphing.gr(normal_pdf, mu=10, sigma=i, min=5, max=15)

# #%%
# # test for significance
# mu_0, sigma_0 = hyptest.normal_approximation_to_binomial(1000, 0.50)
# print("mu_0: {0}, sigma_0: {1}".format(mu_0, sigma_0))
# print(hyptest.normal_two_sided_bounds(0.95, mu=mu_0, sigma=sigma_0), "\n")

# # what happens if the coin is slightly tiled towards heads?
# mu_1, sigma_1 = hyptest.normal_approximation_to_binomial(1000, 0.55)
# print("mu_1: {0}, sigma_1: {1}".format(mu_1, sigma_1))
# print(hyptest.normal_two_sided_bounds(0.95, mu=mu_1, sigma=sigma_1), "\n")

# graphing.gr(normal_pdf, mu=mu_0, sigma=sigma_0, min=450, max=580)
# graphing.gr(normal_pdf, mu=mu_1, sigma=sigma_1, min=450, max=580)

# #%%
# # type 2 error probability: fail to reject the null
# # happens when X is still in our original interval, despite X actually being drawn from H1
# prob_type2 = hyptest.normal_probability_between(
#     *hyptest.normal_two_sided_bounds(0.95, mu=mu_0, sigma=sigma_0),
#     mu=mu_1,
#     sigma=sigma_1
# )

# power = 1 - prob_type2
# print(prob_type2)
# print(power)

# print([(i, 1 - (0.95 ** i)) for i in range(1, 41)])

# graphing.gr(lambda i: 1 - (0.95 ** i), min=1, max=80)


# #%%
# hyptest.two_sided_p_value(529.5, mu=mu_0, sigma=sigma_0)

# graphing.gr(hyptest.two_sided_p_value, mu=mu_0, sigma=sigma_0, min=0, max=1000)


# #%%
# extreme_value_count = 0
# for _ in range(10000):
#     num_heads = sum(1 if random.random() < 0.5 else 0 for _ in range(1000))
#     if num_heads >= 530 or num_heads <= 470:
#         extreme_value_count += 1

# extreme_value_count / 10000


# #%%
# def run_experiment():
#     """ flip a fair coin 1000 times, True = heads, False = tails """
#     return [random.random() < 0.5 for _ in range(1000)]


# def reject_fairness(experiment):
#     """ using the 5% significance levels """
#     num_heads = len([flip for flip in experiment if flip])
#     return num_heads < 469 or num_heads > 531


# random.seed(0)
# experiments = [run_experiment() for _ in range(1000)]
# len([exp for exp in experiments if reject_fairness(exp)])


# #%%
# # Running an A/B test
# # suppose N_A people see ad A, and n_A of them will click it.
# # Each ad is then a Bernoulli trial, where p_A is the probability someone clicks A.


# def estimated_parameters(N, n):
#     """ calculate probability """
#     p = n / N
#     sigma = math.sqrt(p * (1 - p) / N)
#     return p, sigma

# #%%
# # Bayesian Inference
