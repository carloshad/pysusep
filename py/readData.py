"""readData.py - simple Python script for .csv reading."""

import pandas as pd         # loading pandas module
import numpy as np          # loading numpy module
import matplotlib as plt    # loading matplotlib module

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

# reading .csv file into pandas DataFrame object (modify the file path)
df = pd.read_csv('/Users/gustavo/pysusep/csv/LifeInsuranceTable-Australia.csv', header=0)

# taking types and creating an array
office_types = np.array(df.irow(0))

# taking codes and creating an array
office_codes = np.array(df.irow(9))

# printing
print office_types
print office_codes

# deleting word 'Title'
office_types = np.delete(office_types, 0)

# deleting word 'Series ID'
office_codes = np.delete(office_codes, 0)

# updated printing
print office_types
print office_codes
