import tushare as ts
import pandas as pd
import numpy  as np
import datetime
now_stock=ts.get_stock_basics()
filter_stock= now_stock[now_stock.index=='002458']
print filter_stock