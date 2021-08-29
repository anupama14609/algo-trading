import quandl 

appl = quandl.get("WIKI/AAPL", start_date="2006-10-01", end_date="2012-01-01")
print(appl)
appl.to_csv('data/appl_ohlc.csv')