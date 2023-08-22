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

#Return a row as a series
print(df.loc['A'])
print('******************************')

#return several rows
print(df.loc[['A','B']])
print('******************************')

print(df.iloc[0:3])   #slice notation
print('******************************')

#return the value of specific cells
print(df.loc['C','W'])
print('********************************')

print(df.loc[['A','C'],['W','X']])

#selection & filtering
print(df > 0)
print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
print(df[df>0])
print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
print(df['X']>0)
print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
print('Only return rows where X is > 0')
print(df[df['X']>0])
print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')

print(df[(df['W']>0)  &  (df['Y']>0)])
print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')

new_ind = ['WY', 'NY', 'SY', 'Notts', 'Dur']
df['Counties'] = new_ind
print(df)
print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
print(df.set_index('Counties'))  #creates new index called Counties
print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
print(df.describe())