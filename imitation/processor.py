#-*- coding: utf-8 -*-
import tushare as ts
import pandas as pd
import numpy as np
import datetime
import uniout
import time
import random

pledge=50000

filter_list = []
columns = ['code', 'stock_name', 'tail_close','p_change','crotch_number', 'avaliable_crotch_number','unavaliable_crotch_number','profit','now_close','value']

def filter(code, hist, temp,star,end,change):
        now_close=hist.iloc[0]['close']
        tail_close=round(hist.iloc[len(hist)-1]['close']+random.uniform(1,10)/1000,3)
        if  now_close<tail_close: 
            return
        
        p_change=round(np.divide(now_close-tail_close, tail_close)*100,2)
        if p_change<change:
            return

        crotch_number=round(crotch(now_close),0)
        if crotch_number<=0:
            return
        
        profit=round((now_close-tail_close)*crotch_number,3)
        value=round(now_close*crotch_number,3)

        filter_list.append([code,temp['name'],tail_close,p_change,crotch_number,crotch_number,0,profit,now_close,value])
        print 'filter result: code',code,'now_close',now_close,'tail_close',tail_close,'p_change',p_change,'crotch_number',crotch_number,'profit',profit
   

def crotch(price):
    temp_prince=random.uniform(pledge*0.5,pledge)
    temp=np.divide(temp_prince,price)
    if temp<100:
        return 0
    
    return np.floor_divide(temp, 100)*100

def export():
    result= pd.DataFrame(filter_list,columns=columns)
    return result
        
        
    