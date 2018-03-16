#-*- coding: utf-8 -*-  
import tushare as ts
import pandas as pd
import numpy  as np
import datetime
import uniout


filter_list=[]
columns=['code','pe','stardate','enddate','maxdate','maxprice','mindate','minprice','nowprice','fall','up']

pe=20
fall=0.5
up=0.08	
date=-150

nowtime=datetime.datetime.now()
detaday=datetime.timedelta(days=date)
da_days=nowtime+detaday
star=da_days.strftime('%Y-%m-%d')
end=nowtime.strftime('%Y-%m-%d')

now_stock=ts.get_stock_basics()
filter_stock= now_stock[now_stock['pe']<=pe]
for code in filter_stock.index:
    temp=filter_stock.loc[code]
    if   temp['pe']<=0:
        continue
    df= ts.get_hist_data(code,start=star,end=end)
    if df is None:
        continue
    temp_close=df[df['close']>0]['close']
    temp_max=np.max(temp_close)
    temp_min=np.min(temp_close)
    temp_max_df=df[temp_close==temp_max]
    temp_min_df=df[temp_close==temp_min]
    try:
        now_price=df.iloc[0]['close']
    except:
        continue   
    now_fall=np.divide(temp_min, temp_max)
    now_up=np.divide(now_price-temp_min, now_price)
    if now_fall>=fall and now_up>=up:
        print 'code',code,'name',temp['name'].decode('utf-8').encode('gbk'),'pe',temp['pe']
        filter_list.append([code,temp['pe'],star,end,temp_max_df.iloc[0].name,temp_max,temp_min_df.iloc[0].name,temp_min,now_price,now_fall,now_up])

result=pd.DataFrame(filter_list,columns=columns)
result.to_excel('result.xlsx')

