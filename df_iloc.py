import pandas as pd 

df = pd.DataFrame({'x':[1,2,3],'y':[4,5,6],'z':[7,8,9]})
print(f"\nDataFrame Before Updating Index 1 Value:\n{df}")
df.iloc[1] = [10,20,30]
print(f"\nDataFrame After Updating Index 1 Value:\n{df}")