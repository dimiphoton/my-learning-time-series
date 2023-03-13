import pandas_datareader.data as web
import datetime
import pandas as pd 
from functools import reduce

def get_stock(ticker):
    """get a dataframe of stock
    Args:
        ticker (_type_): stock name
    Returns:
        _type_: pandas
    """
    data = web.DataReader(f"{ticker}","yahoo",start,end)
    data[f'{ticker}'] = data["Close"]
    data = data[[f'{ticker}']] 
    print(data.head())
    return data