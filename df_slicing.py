import pandas as pd 
import numpy as np

df = pd.DataFrame(np.random.randn(10,5), columns=['A','B','C','D','E'],index=['a','b','c','d','e','f','g','h','i','j'])
df_slice = df[:]
df_rows_range = df[:5]
df_alternate_cols = df[::2]
df_inverted_index = df[::-1]

print(f'\nDataframe\n{df}')
print(f'\nDataframe with slicing syntax\n{df_slice}')
print(f'\nDataframe with range of rows\n{df_rows_range}')
print(f'\nDataframe with alternate rows\n{df_alternate_cols}')
print(f'\nDataframe with Inverted rows\n{df_inverted_index}')