import quandl 
import pandas as pd

df = pd.read_csv('data/appl_ohlc.csv', header=0, parse_dates=True, index_col='Date')
print(df)