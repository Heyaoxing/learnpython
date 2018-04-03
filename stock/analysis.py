#-*- coding: utf-8 -*-  
import tushare as ts
import pandas as pd
import numpy  as np
import datetime
import pymysql 
import uniout
from sqlalchemy import create_engine


conn = pymysql.connect(host='localhost',user='root',password='123456',db='tushare',charset='utf8')  
sql = 'select * from stock_list'
df = pd.read_sql(sql, con=conn)   



