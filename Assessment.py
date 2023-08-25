import pandas as pd

df = pd.read_csv('african_econ_crises.csv')

print(df.head())

print('\nNames of the {} countries are {} '.format(df['country'].nunique(), df['country'].unique()))

print('\nCountry with the highest cpi inflation rate = {}'
      .format(df.sort_values('inflation_annual_cpi', ascending=False).head(1)['country']))


