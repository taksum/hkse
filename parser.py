# %%
import os
import time
import schedule
import requests
import datetime as dt
import pandas as pd
from utils import isTradable
from config import TICKERS, FEEDS_FOLDER, PARSING_TIME


def run(tickers, feeds_folder = './feeds') -> None:
    date = dt.date.today()
    if isTradable(date):
        for ticker in tickers:
            gotcha = False
            while not gotcha:
                try:
                    feeds_path = os.path.join(feeds_folder, ticker)
                    os.makedirs(feeds_path, exist_ok=True)
                    r = requests.get(f'https://quote.ticker.com.hk/api/historical_data/detail/{ticker}/1d')
                    df = pd.DataFrame(r.json()['data'])
                    df.to_csv(os.path.join(feeds_path, date.strftime('%Y%m%d')+'.csv'), index=False)
                    gotcha = True
                except:
                    print('retrying...')
                    time.sleep(3)
                    pass
        print(f'{date} data is downloaded successfully!')
    else: print(f'{date} is not tradable!')


if __name__ == "__main__":
    print("running...")
    schedule.every().day.at(PARSING_TIME).do(run, TICKERS, FEEDS_FOLDER)
    while True:
        schedule.run_pending()
        time.sleep(30)
