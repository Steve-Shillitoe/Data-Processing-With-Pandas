"""
An exploration of Pandas series.
"""

import numpy as np
import pandas as pd

labels = ['a', 'b', 'c']

myList = [10, 20, 30]

arr = np.array(myList)

dict = {'a':10, 'b':20, 'c':30}

#convert above 3 data structures to Pandas series
print('list to series ', pd.Series(data=myList, index=labels))
print('numpy array to series', pd.Series(data=arr, index=labels))
print('Python dictionary to series', pd.Series(data=dict))

salesQ1 = pd.Series([250, 450, 300, 100], ['USA', 'UK', 'Netherlands', 'Germany'])
print(salesQ1)

salesQ2 = pd.Series([350, 550, 600, 400], ['USA', 'UK', 'Netherlands', 'Japan'])
print(salesQ2)

print(salesQ2['Japan'])

print(salesQ1 + salesQ2)
