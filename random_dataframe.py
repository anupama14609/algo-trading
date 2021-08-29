import pandas as pd 
import numpy as np 

dates = pd.date_range('1/1/2019', periods=8)
df = pd.DataFrame(np.random.randn(8,4),index=dates, columns=['A', 'B', 'C', 'D'])
print(df)