#%%
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import functools
import math

#%%


def gr(f, *args, min=-1, max=1, npoint=1000, **kwargs):
    # TODO: turn gr into a decorator that adds a 'graph' boolean to functions it decorates, where if True calling the function returns a graph of itself and if False calling the function returns its normal output.
    ff = functools.partial(f, *args, **kwargs)
    ff = np.vectorize(ff)
    x_axis = np.linspace(min, max, num=npoint)
    y_axis = ff(x_axis)
    plt.plot(x_axis, y_axis)


def make_hist(f, p, n, num_points):
    data = [f(n, p) for _ in range(num_points)]
    histogram = Counter(data)
    plt.bar(
        [x - 0.4 for x in histogram.keys()],
        [v / num_points for v in histogram.values()],
        0.8,
        color="0.75",
    )
