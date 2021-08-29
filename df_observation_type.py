import quandl 

df = quandl.get("WIKI/AAPL", start_date="2006-10-01", end_date="2012-01-01")
print(df)

df_obs = df['Close'][-10:]
df_obs_type = type(df_obs)
print(df_obs_type)