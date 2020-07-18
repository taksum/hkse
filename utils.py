import holidays
import datetime as dt
import pandas as pd


def isTradable(date: dt.date) -> bool:
    return date not in holidays.CountryHoliday('HK') and date.weekday() < 5


def loadData(ticker: str, start: str, end: str) -> pd.DataFrame:
    return pd.DataFrame()


# Output:
# False
# True
# False
# True
if __name__ == "__main__":
    print(isTradable(dt.date(2020, 7, 1)))
    print(isTradable(dt.date(2020, 7, 2)))
    print(isTradable(dt.date(2020, 7, 12)))
    print(isTradable(dt.date(2020, 7, 13)))
