import pandas as pd 
import numpy as np 

dates = pd.date_range('1/1/2019', periods=8)
df = pd.DataFrame(np.random.randn(8,4),index=dates, columns=['A', 'B', 'C', 'D'])

print("\nDataframe Before Swaping")
print(df)

df[['A','B']] = df[['B','A']]
print("\nDataframe After Swaping - Method 1")
print(df)

df.loc[:, ['A','B']] = df[['B','A']]
print("\nDataframe After Swaping - Method 2")
print(df)

df.loc[:, ['A','B']] = df[['B','A']].to_numpy()
print("\n Preferred Way To Swap Columns of Dataframe - Method 3")
print(df)