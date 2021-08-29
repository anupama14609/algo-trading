import pandas as pd

df = pd.read_csv('data/df_ohlc.csv', parse_dates=True)
print(df)