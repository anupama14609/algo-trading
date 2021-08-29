import pandas as pd
import numpy as np 

df = pd.DataFrame(np.random.randn(10,5))
print(df)

labeled_df = pd.DataFrame(np.random.randn(10,5), columns=['A','B','C','D','E'])
print(labeled_df)
