# %%
from utils import *
from trading import random
from performance import *
from config import STRATS_PARAMS, FEEDS_FOLDER


start_date = '20200715'
end_date = '20200721'

tickers = [
    '9988',
    '388',
    '5'
]

strats =[
    random,
]

for ticker in tickers:
    dataframes = loadData(ticker, start_date, end_date, FEEDS_FOLDER)
    result = {}
    for strat in strats:
        for df in dataframes:
            ts = calTickSize(df)
            # TODO: strat config dot product
            df = strat(df, ts)
            evaluate(df, strat, result)
    visualize(result)
