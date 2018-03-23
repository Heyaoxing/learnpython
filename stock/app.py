#-*- coding: utf-8 -*-
import tushare as ts
import pandas as pd
import numpy as np
import datetime
import uniout
import fall as fa
import pullup as pu


date = -365
nowtime = datetime.datetime.now()
detaday = datetime.timedelta(days=date)
da_days = nowtime+detaday
star = da_days.strftime('%Y-%m-%d')
end = nowtime.strftime('%Y-%m-%d')


now_stock = ts.get_stock_basics()
filter_stock = now_stock[now_stock['pe'] != 0]
for code in filter_stock.index:
    temp = filter_stock.loc[code]
    hist = ts.get_hist_data(code, start=star, end=end)
    pu.process(code, hist, temp)
pu.commit()
print 'end'
