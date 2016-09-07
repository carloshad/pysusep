"""readData.py - Python script to read .csv, clean it and export it.

Authors: Gustavo CPO & Carlos HAD
Date: Sep 7, 2016

"""

import pandas as pd                  # loading pandas module
import numpy as np                   # loading numpy module
import os.path                       # loading os.path to work with paths
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
'''

''' STEP 1: Read the .csv file. '''

# getting file path in your OS
fid = os.path.join(os.path.dirname(__file__),
      '../csv/LifeInsuranceTable-Australia-Clean.csv')

# reading .csv file into pandas DataFrame object
df = pd.read_csv(fid, header=None)

# filling missing entries of original file with 0's
df.fillna(value=0, inplace=True)


''' STEP 2: Modify headers to clean the file.'''

# getting header names and creating an array
header_names = np.array(df.iloc[0])

# replacing name 'SeriesID' with 'Time'
header_names[0] = 'Time'

''' Removing string to reduce the header names. '''

# string to remove
strAux = 'Life insurance offices; '

# finding strAux and removing it out
for i in range(1, header_names.shape[0]):
    aux = header_names[i]
    aux = aux[len(strAux):]
    header_names[i] = aux

''' STEP 3: Create a new dictionary object to build a new DataFrame.'''

''' Filling (key,values) pair to build a new dict. '''

# declare empty variables
keys = []
values = []
for i in range(0, header_names.shape[0]):

    # filling keys
    keys.append(header_names[i])

    # getting Series (i-th column)
    aux = df.iloc[:, i]

    # convert to numpy object
    aux = aux.as_matrix()

    # removes two first lines out
    aux = aux[2:]

    # conversions
    if i == 0:  # 1st column: string
        aux = aux.astype(str)
    else:   # 2nd column and on: integers
        aux = aux.astype(int)

    # filling values
    values.append(aux)

# creating ordered dict to keep the same
# non-alphabetical order of the original file
newDict = OrderedDict(zip(keys, values))

# create new dataframe from 'newDict'
dfNew = pd.DataFrame(newDict)

''' STEP 4: Export new DataFrame to new .csv file'''

# file path to new file
fidOut = os.path.join(os.path.dirname(__file__),
        '../csv/LifeInsuranceTable-Australia-New.csv')

# export
dfNew.to_csv(fidOut, columns=header_names)

# message
print 'You did it! Check the new file in: ' + fidOut + '.'
