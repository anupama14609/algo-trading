import pandas as pd

df = pd.read_csv('data/df_ohlc.csv',index_col='Date')
print(df)