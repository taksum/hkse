import utils
import datetime as dt

def test_isTradable():
    assert(utils.isTradable(dt.date(2020, 7, 1)) == False)
    assert(utils.isTradable(dt.date(2020, 7, 2)) == True)
    assert(utils.isTradable(dt.date(2020, 7, 12)) == False)
    assert(utils.isTradable(dt.date(2020, 7, 13)) == True)