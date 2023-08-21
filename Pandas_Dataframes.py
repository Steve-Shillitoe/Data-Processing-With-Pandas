import numpy as np
from numpy.random import randint
import pandas as pd

columns = ['W', 'X', 'Y', 'Z']
index = ['A', 'B', 'C', 'D', 'E']

np.random.seed(42)
data = randint(-100, 100, size=(5,4))

df = pd.DataFrame(data, index, columns)
print(df)
print('******************')

#To return a series
print(df['W'])
print('******************')
print(df[['W', 'X']])

#Feature engineering
#Add a new column to DF
df['New'] = df['W'] + df['X']
print(df)
print('******************')

#Remove a column from the DF
df = df.drop('New', axis=1) # axis=1 drop a column, axis=0 drop a row
print(df)
print('******************')




