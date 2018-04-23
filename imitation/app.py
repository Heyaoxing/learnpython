#-*- coding: utf-8 -*-
import tushare as ts
import pandas as pd
import numpy as np
import datetime
import uniout
import processor as pro
import toemail as email
import sys
import loghelper as logging
change=20
date = -15
nowtime = datetime.datetime.now()
detaday = datetime.timedelta(days=date)
da_days = nowtime+detaday
star = da_days.strftime('%Y-%m-%d')
end = nowtime.strftime('%Y-%m-%d')


now_stock = ts.get_stock_basics()
filter_stock = now_stock[now_stock['pe'] != 0]

for code in filter_stock.index:
    try:
        temp = filter_stock.loc[code]
        hist = ts.get_hist_data(code, start=star, end=end)
        if hist is None or hist.index is None or temp['pe'] <= 0:
            continue
        if hist is None:
            continue
        pro.filter(code, hist, temp,star,end,change)

    except:
        print '\n======except!! code is ',code

result=pro.export() 
email.tosend(result,star,end)
logging.info('完成时间'+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print 'end'