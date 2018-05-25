
import tushare as ts
import pandas as pd
import numpy as np
import datetime
import uniout
import urllib2
from bs4 import BeautifulSoup
import sys   
reload(sys)

date = -7
nowtime = datetime.datetime.now()
detaday = datetime.timedelta(days=date)
da_days = nowtime+detaday
star = da_days.strftime('%Y-%m-%d')
end = nowtime.strftime('%Y-%m-%d')

df=ts.get_hist_data("603676")
print df
# if df is None:
#     print 'None'
# length=len(df)-1
# index=0
# isTrue=False
# while(length>index):
#     maxval=max(df.iloc[index]['open'],df.iloc[index]['close'])
#     minval=min(df.iloc[index]['open'],df.iloc[index]['close'])
#     change= (maxval-minval)/minval*100
#     if change>2:
#         print '1',change,maxval,minval,df.iloc[index].name
#         index=index+1
#         continue
#     if maxval>=df.iloc[index]['high'] or minval<=df.iloc[index]['low']:
#         print '2',maxval,df.iloc[index]['high'],minval,df.iloc[index]['low']
#         index=index+1
#         continue
#     if df.iloc[index+1]['p_change']<9.9:
#         print '3',df.iloc[index+1]['p_change']
#         index=index+1
#         continue
#     if df.iloc[index+1]['high']>df.iloc[index]['close']:
#         print '4'
#         index=index+1
#         continue
#     if df.iloc[index+1]['volume']>df.iloc[index]['volume']:
#         print '5'
#         index=index+1
#         continue   
#     index=index+1
#     isTrue=True

# print isTrue