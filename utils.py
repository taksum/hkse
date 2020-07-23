import holidays
import datetime as dt
import pandas as pd


def isTradable(date: dt.date) -> bool:
    return date not in holidays.CountryHoliday('HK') and date.weekday() < 5


def loadData(ticker: str, start: str, end: str) -> pd.DataFrame:
    return pd.DataFrame()