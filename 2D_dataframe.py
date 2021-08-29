import pandas as pd 
import numpy as np 

df = pd.DataFrame({'x':[1,2,3,4,5],'y':[5,4,3,2,1]})
df_labeled = pd.DataFrame({'x':[1,2,3,4,5],'y':[5,4,3,2,1]}, index=['A','B','C','D','E'])

print(f"\nDataframe With Default Index Label:\n{df}")
print(f"\nDataframe With Defined Index Label:\n{df_labeled}")