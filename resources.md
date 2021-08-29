Date@290821
=======================================================================================
Notes...............
pandas-datareader package allows for reading in data from sources such as Google, World Bank. 
"pandas_datareader to import data into your workspace"
To access updated data from Yahoo! Finance, is been depricated. 
pip install jupyterthemes
pandas_datareader - package used to pull in financial data
quandl - another package to get data from Google Finance
Volume - column is used to register the number of shares that got traded during a single day
Adj Close - the adjusted closing price: it’s the closing price of the day that has been slightly adapted to include any actions that occurred at any time before the next day’s open

DataFrame structure was a two-dimensional labeled array with columns that potentially hold different types of data.
Pandas doesn't allow Series to be assigned into nonexistent columns

Using loc with missing keys in a list is Deprecated.

pandas provides a suite of methods in order to have purely label based indexing. This is a strict inclusion based protocol. Every label asked for must be in the index, or a KeyError will be raised. When slicing, both the start bound AND the stop bound are included, if present in the index. 

References..........................................................
https://www.datacamp.com/community/tutorials/finance-python-trading
https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html
