#-*- coding: utf-8 -*-
import tushare as ts
import pandas as pd
import numpy as np
import datetime
import uniout
import time
from sqlalchemy import create_engine

# add_date = -7
# offset_date=0
# nowtime = datetime.datetime.now()
# star_detaday = datetime.timedelta(days=add_date)
# end_detaday = datetime.timedelta(days=offset_date)
# star = (nowtime+star_detaday+end_detaday).strftime('%Y-%m-%d')
# end =  (nowtime+end_detaday).strftime('%Y-%m-%d')

nowtime = datetime.datetime.now()
area=['辽宁','吉林','内蒙古','黑龙江']
filter_list = []
columns = ['code', 'tname', 'pe','turnover', 'nowprice','change','kline','tip']
dict = {'30': 'sz', '20': 'sz', '90': 'sh', '00': 'sz', '60': 'sh'}
def filter(code, hist, temp,star,end):
    if hist is None or hist.index is None or temp['pe'] <= 0:
        return

    df= hist[(hist.index>=star)&(hist.index<=end)]
    if df is None:
        return
    print 'filter code',code
    length=len(df)-1
    index=0
    isTrue=False
    tip=''
    while(length>index):
        maxval=max(df.iloc[index]['open'],df.iloc[index]['close'])
        minval=min(df.iloc[index]['open'],df.iloc[index]['close'])
        change= (maxval-minval)/minval*100
        if change>0.7:
            index=index+1
            continue
        if maxval>=df.iloc[index]['high'] or minval<=df.iloc[index]['low']:
            index=index+1
            continue
        if df.iloc[index+1]['p_change']<9.9:
            index=index+1
            continue
        if df.iloc[index+1]['high']>df.iloc[index]['close']:
            index=index+1
            continue
        if df.iloc[index+1]['volume']>df.iloc[index]['volume']:
            index=index+1
            continue
        
        if (df.iloc[index+1]['close']-df.iloc[index+1]['open'])/df.iloc[index+1]['open']*100<8:
            index=index+1
            continue
        if (minval-df.iloc[index+1]['close'])/df.iloc[index+1]['close']*100<0.8:
            index=index+1
            continue
        
        if df.iloc[index]['ma5']>df.iloc[index+1]['ma5'] and df.iloc[index]['ma10']>df.iloc[index+1]['ma10'] and df.iloc[index]['ma20']>df.iloc[index+1]['ma20']:   
            tip=tip+' 出现十字星放量日期为:'+df.iloc[index].name
            isTrue=True  
        index=index+1

    if isTrue==False:
        return 

    
    if temp['industry'].decode('utf-8').encode('gbk') in area:
        tip=tip+' 东北票'   
    if temp['area'].find('银行')!=-1 or temp['name'].find('银行')!=-1:
        tip=tip+' 银行票'  
    if temp['name'].find('ST')!=-1:
        tip=tip+' ST票' 
    if df.iloc[0]['p_change']>9.5:
        tip=tip+' 涨幅过大'         

    kline='http://image.sinajs.cn/newchart/daily/n/'+ dict.get(code[0:2])+code+'.gif'
    now_price=df.iloc[0]['close']
    print 'filter result: code',code,'name',temp['name'].decode('utf-8').encode('gbk'),'pe',temp['pe'],'tip',tip
    filter_list.append([code,temp['name'],temp['pe'],df.iloc[0]['turnover'],now_price,df.iloc[0]['p_change'],kline,tip])


def export():
    result= pd.DataFrame(filter_list,columns=columns)
    return result
        