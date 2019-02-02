# Count words in input and then write out the most common

import sys
from collections import Counter, OrderedDict

print('\n')

inp = sys.argv[1]

num = Counter(inp.split(' '))
print(num)
