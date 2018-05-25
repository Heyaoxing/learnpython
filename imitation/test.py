
import tushare as ts
import pandas as pd
import numpy as np
import datetime
import uniout
import urllib2
from bs4 import BeautifulSoup
import sys   
reload(sys)

date = -180
nowtime = datetime.datetime.now()
detaday = datetime.timedelta(days=date)
da_days = nowtime+detaday
star = da_days.strftime('%Y-%m-%d')
end = nowtime.strftime('%Y-%m-%d')

df=ts.get_hist_data("002458",star,end)
if df is None:
    print 'None'
length=len(df)-1
index=0
isTrue=False
tip=''
while(length>index):
        maxval=max(df.iloc[index]['open'],df.iloc[index]['close'])
        minval=min(df.iloc[index]['open'],df.iloc[index]['close'])
        change= (maxval-minval)/minval*100
        if change > 0.5:
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
            tip=tip+' 出现十字星放量日期为:' + df.iloc[index].name
            isTrue=True  
        index=index+1

print isTrue