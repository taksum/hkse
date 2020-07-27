import os
import holidays
import datetime as dt
import pandas as pd
from itertools import product


def isTradable(date) -> bool:
    if type(date) is str:
        date = dt.datetime.strptime(date, '%Y%m%d')
    return date not in holidays.CountryHoliday('HK') and date.weekday() < 5


def loadData(ticker, start='', end='', feeds_folder='./feeds') -> list:
    """Read csv files from feeds folder.

    Args:
        ticker       (str): A stock ticker
        start        (str): A start date
        end          (str): A end date
        feeds_folder (str): A folder storing feeds

    Returns:
        l           (list): A list of pandas DataFrame object

    """
    old_cwd = os.getcwd()
    os.chdir(os.path.join(feeds_folder, ticker))

    l = []
    for file in os.listdir():
        if not start and not end:
            l.append(pd.read_csv(file, index_col=0))
        elif not start:
            if file[:-4] <= end:
                l.append(pd.read_csv(file, index_col=0))
        elif not end:
            if start <= file[:-4]:
                l.append(pd.read_csv(file, index_col=0))
        else:
            if start <= file[:-4] <= end:
                l.append(pd.read_csv(file, index_col=0))

    os.chdir(old_cwd)

    return l


def calTickSize(df: pd.DataFrame) -> float:
    """Calculate tick size from dataframe.

    Args:
        df     (DataFrame): Price data of a stock

    Returns:
        ts         (float): Tick size of the stock 

    """
    tick_table = {
        0.25: 0.001,
        0.5 : 0.005,
        10  : 0.010,
        20  : 0.020,
        100 : 0.050,
        200 : 0.100,
        500 : 0.200,
        1000: 0.500,
        2000: 1.000,
        5000: 2.000,
        9999: 5.000
    }
    open_price = df['open'].iloc[0]
    for p, ts in tick_table.items():
        if open_price <= p:
            return ts


def dotProduct(l: list) -> list:
    """
    Args:
        l          (list): list of list containing parameters
        
    Returns:
        dot        (list): list of dot products 
    """
    dot = list(product(*l))
    return dot
    
