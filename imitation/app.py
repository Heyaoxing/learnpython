#-*- coding: utf-8 -*-
import tushare as ts
import pandas as pd
import numpy as np
import datetime
import uniout
import selectten as se
import toemail as email
import sys
import loghelper as logging


logging.info('开始时间:'+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

date =-180
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
        if hist is None :
            continue
        if hist is None:
            continue
        se.filter(code, hist, temp,star,end) 

    except Exception,err:
        print '\n======except!! code is ',code,' ',err

result=se.export() 
email.tosend(result,star,end,'730530507@qq.com')
email.tosend(result,star,end,'1987613740@qq.com')
logging.info('完成时间:'+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print 'end'