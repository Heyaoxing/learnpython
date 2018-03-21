#-*- coding: utf-8 -*-
import tushare as ts
import pandas as pd
import numpy as np
import datetime
import uniout
import time
from sqlalchemy import create_engine
fall = 0.5
up = 0.08

date = -150
nowtime = datetime.datetime.now()
detaday = datetime.timedelta(days=date)
da_days = nowtime+detaday
star = da_days.strftime('%Y-%m-%d')
end = nowtime.strftime('%Y-%m-%d')

filter_list = []
columns = ['code', 'name', 'pe', 'stardate', 'enddate', 'maxdate',
    'maxprice', 'mindate', 'minprice', 'nowprice', 'fall', 'up']


def process(code, hist, temp):
    try:
        if hist is None or hist.index is None or temp['pe'] <= 0:
                return
        df= hist[(hist.index>=star)&(hist.index<=end)]
        if df is None:
            return
        temp_close=df[df['close']>0]['close']
        temp_max=np.max(temp_close)
        temp_min=np.min(temp_close)
        temp_max_df=df[temp_close==temp_max]
        temp_min_df=df[temp_close==temp_min]
        
        now_price=df.iloc[0]['close']
        
        now_fall=np.divide(temp_min, temp_max)
        now_up=np.divide(now_price-temp_min, now_price)
        if now_fall>=fall and now_up>=up:
            print 'code',code,'name',temp['name'].decode('utf-8').encode('gbk'),'pe',temp['pe']
            filter_list.append([code,temp['name'],temp['pe'],star,end,temp_max_df.iloc[0].name,temp_max,temp_min_df.iloc[0].name,temp_min,now_price,now_fall,now_up])
    except:
        print '\n======except!! code is ',code
        return 

def insert():
    result=pd.DataFrame(filter_list,columns=columns)
    engine = create_engine('mysql://root:123456@127.0.0.1/tushare?charset=utf8')
    result.to_sql('fall_data',engine,if_exists='replace')

def commit():
    try:
        insert()
    except: 
        print 'commit again'
        insert()
