#-*- coding: utf-8 -*-
import tushare as ts
import pandas as pd
import numpy as np
import datetime
import uniout

now_stock =ts.get_hist_data('600009')
print now_stock.iloc[0]['close']
print now_stock.iloc[len(now_stock)-1]['close']