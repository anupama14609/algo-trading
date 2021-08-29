import quandl 
import pandas as pd 

df = quandl.get("WIKI/AAPL", start_date="2006-10-01", end_date="2012-01-01")

print("\n Inspecting the first rows of November-December 2006\n")
print(df.loc[pd.Timestamp('2006-11-01'):pd.Timestamp('2006-12-31')].head())

print("\n Inspecting the first rows of 2007\n")
print(df.loc['2007'].head())

print("\n Inspecting the rows of 2006\n")
print(df.loc['2006'])

print("\n Inspecting the November 2006")
print(df.iloc['22:43'])

print("\n  Inspect the 'Open' and 'Close' values at 2006-11-01 and 2006-12-01 \n")
print(df.iloc[[22,43], [0, 3]])