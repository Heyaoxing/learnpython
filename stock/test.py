import tushare as ts
import pandas as pd
import numpy as np
import datetime
import time

df = ts.get_hs300s()
temp=df[df['code']=='600009']

print temp['code']

