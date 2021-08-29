import pandas_datareader.data as pdr 
import datetime as dt 

start = dt.datetime(2015,1,1)
end = dt.datetime(2020,1,31)

df = pdr.get_data_yahoo('AAPL', start, end)
print(df)

df_cols = df.columns
print(df_cols)


