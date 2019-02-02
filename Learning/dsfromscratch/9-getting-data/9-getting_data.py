#!/usr/bin/env python
# coding: utf-8

# # Getting Data

# Here's how to get data using python's standard library.

# ## stdin and stdout

# In[13]:
# In[16]:


# Make a script that reads in lines of text and spits out the ones that match a regular expression
# Turn this ipynb file into a python script after I'm done, then test on the command line

import sys, re

regex = sys.argv[1]

for line in sys.stdin:
    if re.search(regex, line):
        sys.stdout.write(line)