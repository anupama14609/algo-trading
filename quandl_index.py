import quandl 
df = quandl.get("WIKI/AAPL", start_date="2006-10-01", end_date="2012-01-01")
print(df)

df_index =df.index
print(df_index)