"""
This module explores how Pandas can be used to deal with missing data.
"""

import numpy as np
import pandas as pd

df = pd.DataFrame({'A':[1, 2,np.nan, 4],
                   'B':[5, np.nan, np.nan,8],
                   'C':[10,20,30,40]   } )

print(df)

#drop data
print(df.dropna(axis=1, thresh=3))

#Fill in the missing values
print(df.fillna(value='Fill Value'))
