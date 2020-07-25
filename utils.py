import os
import holidays
import datetime as dt
import pandas as pd


def isTradable(date: dt.date) -> bool:
    return date not in holidays.CountryHoliday('HK') and date.weekday() < 5


def loadData(ticker, start='', end='', feeds_folder='./feeds') -> pd.DataFrame:
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
