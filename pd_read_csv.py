import pandas as pd

df = pd.read_csv('data/df_ohlc.csv', header=0, index_col='Date', parse_dates=True)
print(df)