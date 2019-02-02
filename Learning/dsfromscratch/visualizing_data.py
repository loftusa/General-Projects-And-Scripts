# Make a simple plot with matplotlib
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(101)
y = x ** 2

# Make the line green, give it titles
# plt.plot(x, y, color="green",)
# plt.xlabel('x axis')
# plt.ylabel('y axis')
# plt.title('x plotted against y with a green color')

# make a bar chart
x = {
    "Annie Hall": 5,
    "Ben-Hur": 11,
    "Casablanca": 4,
    "Gandhi": 9,
    "West Side Story": 10,
}
# plt.bar(x.keys(), x.values())
# plt.show()

# Not gonna finish this chapter for now, moving on to the linear algebra chapter because I think it'll be more helpful.
# Already know matplotlib well enough to figure stuff out.

print(__name__)
