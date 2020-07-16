# %%
import os
import time
import datetime
import schedule
import requests
import holidays
import pandas as pd

parsing_time = '17:30'
feeds_folder = '.\\feeds'
url = 'https://quote.ticker.com.hk/api/historical_data/detail/{}/1d'
tickers = [
    '5',
    '27',
    '175',
    '388',
    '700',
    '788',
    '981',
    '1299',
    '1810',
    '1833',
    '1928',
    '2018',
    '2318',
    '2382',
    '3690',
    '9618',
    '9988',
    'HSI.HK',
]


def isTradable(date):
    return date not in holidays.CountryHoliday('HK') and date.weekday() < 5


def get(ticker, date):
    feeds_path = os.path.join(feeds_folder, ticker, date)
    os.makedirs(feeds_path, exist_ok=True)

    file_path = os.path.join(feeds_path, '{}.csv'.format(date))
    if os.path.exists(file_path): return

    r = requests.get(url.format(ticker))
    df = pd.DataFrame(r.json()['data'])
    df.to_csv(file_path, index=False)


def run():
    date = datetime.date.today()
    if isTradable(date):
        for ticker in tickers:
            got = False
            while not got:
                try:
                    get(ticker, date.strftime('%Y%m%d'))
                    got = True
                except:
                    print('retrying...')
                    time.sleep(3)
                    pass
        print("{} data downloaded successfully!".format(date))
    else:
        print("{} is not tradable!".format(date))


if __name__ == "__main__":
    print("running...")
    schedule.every().day.at(parsing_time).do(run)
    while True:
        schedule.run_pending()
        time.sleep(30)
