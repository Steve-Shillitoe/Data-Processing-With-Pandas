"""
An exploration of the Pandas groupby function
"""
import pandas as pd

df = pd.read_csv('Universities.csv')

print(df.head())

#Mean number of completions per year (Year is a category, Completions is continuous)
print(df.groupby('Year').mean('Completions'))
print('**********************************************')

#Group by multiple categories. Outer index is 'Year', inner index is 'Sector'
print(df.groupby(['Year', 'Sector']).sum('Completions'))
print('**********************************************')

#Output aggregate statistics for completions each year
print(df.groupby('Year').describe().transpose())
print('**********************************************')