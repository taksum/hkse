# %%
import os
import time
import schedule
import requests
from utils import isTradable
from config import TICKERS, FEEDS_FOLDER
import datetime as dt
import pandas as pd

PARSING_TIME = '17:30'
URL          = 'https://quote.ticker.com.hk/api/historical_data/detail/{}/1d'

def get(ticker: str, date: dt.date, url: str, feeds_folder: str) -> None:
    feeds_path = os.path.join(feeds_folder, ticker)
    os.makedirs(feeds_path, exist_ok=True)
    file_path = os.path.join(feeds_path, '{}.csv'.format(date))
    
    if not os.path.exists(file_path):
        r = requests.get(url.format(ticker))
        df = pd.DataFrame(r.json()['data'])
        df.to_csv(file_path, index=False)

def run(tickers, url: str, feeds_folder: str) -> None:
# migrate to with python 3.9:
# def run(tickers: list[str], url: str, feeds_folder: str) -> None:
    date = dt.date.today()
    if isTradable(date):
        for ticker in tickers:
            gotcha = False
            while not gotcha:
                try:
                    get(ticker, date.strftime('%Y%m%d'), url, feeds_folder)
                    gotcha = True
                except:
                    print('retrying...')
                    time.sleep(3)
                    pass
        print("{} data downloaded successfully!".format(date))
    else: print("{} is not tradable!".format(date))


if __name__ == "__main__":
    print("running...")
    schedule.every().day.at(PARSING_TIME).do(run, TICKERS, URL, FEEDS_FOLDER)
    while True:
        schedule.run_pending()
        time.sleep(30)
