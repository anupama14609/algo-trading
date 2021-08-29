import quandl 
import pandas as pd 
df = quandl.get("WIKI/AAPL", start_date="2006-10-01", end_date="2012-01-01")

df_loc = df.loc[pd.Timestamp('2006-11-01'):pd.Timestamp('2006-12-31')]
print(df_loc)