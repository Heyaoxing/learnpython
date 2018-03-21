#-*- coding: utf-8 -*-
import tushare as ts
import pandas as pd
import numpy as np
import datetime
import uniout
import time
from sqlalchemy import create_engine

add_date = -7
offset_date=-2
nowtime = datetime.datetime.now()
star_detaday = datetime.timedelta(days=add_date)
end_detaday = datetime.timedelta(days=offset_date)
star = (nowtime+star_detaday+end_detaday).strftime('%Y-%m-%d')
end =  (nowtime+end_detaday).strftime('%Y-%m-%d')
global a
a = 3

filter_list = []
columns = ['code', 'name', 'pe', 'stardate', 'enddate', 'maxdate',
    'maxprice', 'mindate', 'minprice', 'nowprice']

def process(code, hist, temp):
    try:
        if hist is None or hist.index is None or temp['pe'] <= 0:
            return
        df= hist[(hist.index>=star)&(hist.index<=end)]
        if df is None:
            return
        filter_df_change=df.iloc[0]['p_change']
        filter_df_len=len(df[df['p_change']>1])
        if filter_df_change<3 or filter_df_len<3:
            return
        now_price=df.iloc[0]['close']
        temp_close=df[df['close']>0]['close']
        temp_max=np.max(temp_close)
        temp_min=np.min(temp_close)
        temp_max_df=df[temp_close==temp_max]
        temp_min_df=df[temp_close==temp_min]
        print 'filter result: code',code,'name',temp['name'].decode('utf-8').encode('gbk'),'pe',temp['pe']
        filter_list.append([code,temp['name'],temp['pe'],star,end,temp_max_df.iloc[0].name,temp_max,temp_min_df.iloc[0].name,temp_min,now_price])
        
        temp_head=hist.head(2)
        if len(temp_head[temp_head['p_change']>2])>0 :  
            print 'valid filter result: code',code,'name',temp['name'].decode('utf-8').encode('gbk'),'pe',temp['pe']
            global a
            a=1+a


    except:
        print '\n======except!! code is ',code
        return

def insert():
    result=pd.DataFrame(filter_list,columns=columns)
    proportion=np.divide(a, len(result))
    print '======================proportion============================'
    print 'proportion:',proportion
    engine = create_engine('mysql://root:123456@127.0.0.1/tushare?charset=utf8')
    result.to_sql('pullup_data',engine,if_exists='replace')


def commit():
    try:
        insert()
    except: 
        print 'commit again'
        insert()
    