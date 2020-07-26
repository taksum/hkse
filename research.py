# %%
import pandas as pd
import numpy as np
from utils import *
from trading import random
from performance import *
from config import STRATS_CONFIG


tickers = [
    '9988',
    '388',
    '5'
]

strats =[
    random,
]

for ticker in tickers:
    dataframes = loadData(ticker)
    result = {}
    for strat in strats:
        for df in dataframes:
            ts = calTickSize(df)
            # TODO: strat config dot product
            df = strat(df, ts)
            evaluate(df, strat, result)
    visualize(result)
