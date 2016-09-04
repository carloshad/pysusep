"""readData.py - simple Python script for .csv reading."""

import pandas as pd                  # loading pandas module
import numpy as np                   # loading numpy module
import matplotlib as plt             # loading matplotlib module
import os.path                       # loading os.path to work with paths on your OS
from collections import OrderedDict  # to work with ordered dictionaries

'''
Action required: install 'pandas','numpy' and 'matplotlib' into
Python's module list. At command line, type:

pip install pandas
pip install numpy
pip install matplotlib

--- PANDAS
Python Data Analysis Library
pandas is an open source, BSD-licensed library providing
high-performance, easy-to-use data structures and data
analysis tools for the Python programming language.
http://pandas.pydata.org
---

--- NUMPY
NumPy is the fundamental package for scientific computing with Python.
It contains among other things:
    - a powerful N-dimensional array object
http://www.numpy.org
---

--- MATPLOTLIB
Matplotlib is a python 2D plotting library which produces quality figures.
Useful for data visualization.
http://matplotlib.org
---
'''

# file path
fid = os.path.join(os.path.dirname(__file__),
      '../csv/LifeInsuranceTable-Australia-Clean.csv')

# reading .csv file into pandas DataFrame object
df = pd.read_csv(fid, header=None)

# fill missing entries with N/A
df.fillna

# getting names and creating an array
header_names = np.array(df.iloc[0])

# replacing 'SeriesID' with 'Time'
header_names[0] = 'Time'

# removing string to reduce names
strAux = 'Life insurance offices; '

for i in range(1, header_names.shape[0]):
    aux = header_names[i]
    aux = aux[len(strAux):]
    header_names[i] = aux

'''
INCOMPLETE!!!

What to do?

Creating a ordered dictionary with new names in order to create a new
dataframe to be exported. We need to fill in the dictionary with
'key:value' pairs:
 - the keys should be the new names
 - the values should be the columns

Can this be done through a multiindex 'for' to fill in the dictionary?

 '''

# getting csv data from 10th line and on for all columns
# aux = df.iloc[10:, :]

# A 'for' in j is required to run over columns!
# df.iloc[10:, j]
#newDict = OrderedDict((i, aux) for i in header_names)
#newDict = OrderedDict((i, j) for i, j in header_names, df.iloc[10:, j]))

'''
After creating the new dataframe 'newDict', we export
the new .csv to directory

dfNew = pd.DataFrame(newDict)
fidOut = os.path.join(os.path.dirname(__file__),
        '../csv/LifeInsuranceTable-Australia-New.csv')
dfNew.to_csv(fidOut, columns=header_names)
'''
