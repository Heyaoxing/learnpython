#-*- coding: utf-8 -*-  
import tushare as ts
import pandas as pd
import numpy  as np
import datetime
import uniout
from sqlalchemy import create_engine


stock_concept=ts.get_concept_classified()
stock_hs300s=ts.get_hs300s()
stock_sz50s=ts.get_sz50s()
stock_zz500s=ts.get_zz500s()

stock_list=ts.get_stock_basics()

stock_list['concept_name']=''
stock_list['ishs300s']=0
stock_list['issz50s']=0
stock_list['iszz500s']=0
for code in stock_list.index:
    temp_con=stock_concept[stock_concept['code']==code]
    temp_hs300s=stock_hs300s[stock_hs300s['code']==code]
    temp_sz50s=stock_sz50s[stock_sz50s['code']==code]
    temp_zz500s=stock_zz500s[stock_zz500s['code']==code]
    if len(temp_con)>0:
        stock_list.loc[code]['concept_name']=temp_con['c_name']
    else:
        stock_list.loc[code]['concept_name']=''
        print 'concept_name insert'
    
    if len(temp_hs300s)==0:
        stock_list.loc[code]['ishs300s']=0
    else:
        stock_list.loc[code]['ishs300s']=1
        print 'temp_hs300s insert'

    if len(temp_sz50s)==0:
            stock_list.loc[code]['issz50s']=0
    else:
        stock_list.loc[code]['issz50s']=1    
        print 'issz50s insert'

    if len(temp_zz500s)==0:
            stock_list.loc[code]['iszz500s']=0
    else:
        stock_list.loc[code]['iszz500s']=1
        print 'iszz500s insert'

stock_list['code']=stock_list.index
stock_list.index = range(1,len(stock_list) + 1)

engine = create_engine('mysql://root:123456@127.0.0.1/tushare?charset=utf8')
stock_list.to_sql('stock_list',engine,if_exists='replace')

