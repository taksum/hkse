import pandas as pd
import numpy as np


def random(df, numTriggers=200, ts=50):
    df['val'] = df['close'] + np.random.normal(0, 20)
    df['offset'] = df['val'] - ts
    return df
