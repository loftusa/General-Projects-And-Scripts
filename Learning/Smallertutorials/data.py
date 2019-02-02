%matplotlib inline
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = 'all'
plt.style.use('seaborn')

import os
from urllib.request import urlretrieve

FREMONT_URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'

def get_fremont_data(filename='Fremont.csv', url=URL, force_download=False):
	
	"""
	Download and cache Fremont data

	Parameters
	-----------
	filename: string (optional)
		location to save data
	url : string (optional)
	force_download : bool (optional)
		if True, force redownload of data

	Returns
	-------
	data: pandas.DataFrame
		The fremont bridge data
	"""

    if force_download or not os.path.exists(filename):
        urlretrieve(URL, 'Fremont.csv')
    data = pd.read_csv('Fremont.csv', index_col='Date', parse_dates=True)
    data.columns = ['West', 'East']
    data['Total'] = data['West'] + data['East']
    return data