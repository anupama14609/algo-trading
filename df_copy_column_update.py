import pandas as pd 
import numpy as np 

dates = pd.date_range('1/1/2019', periods=8)
df = pd.DataFrame(np.random.randn(8,4),index=dates, columns=['A', 'B', 'C', 'D'])
dfa = df.copy()

print(f"\nCopied Dataframe Before Updating Column Data\n{dfa}")

dfa.A = list(range(len(dfa.index)))
df_update = dfa.A

print(f"\nCopied Dataframe Updated Column Data\n{df_update}")
print(f"\nCopied Dataframe Before Updating Column Data\n{dfa}")