import pandas as pd 

df = pd.DataFrame({'x':[1,2,3],'y':[4,5,6],'z':[7,8,9]})
print(f"\nDataFrame Before updating Value at index 1:\n{df}")

df.iloc[1] = [10,20,30]
print(f"\nDataFrame After updating Value at index 1:\n{df}")

df_data = df.loc[:]
df_loc = df.loc[2]
df_iloc = df.iloc[2]
print(f"\nAccessing DataFrame using pandas's loc method:\n{df_data}")
print(f"\nAccessing DataFrame Column's value using pandas's loc method:\n{df_loc}")
print(f"\nAccessing DataFrame Column's value using pandas's iloc method:\n{df_iloc}")