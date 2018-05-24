
import tushare as ts
import pandas as pd
import numpy as np
import datetime
import uniout
import urllib2
from bs4 import BeautifulSoup
import sys   
reload(sys)
sys.setdefaultencoding('utf-8')  



def math_test(price,a):
    a=a+1
    print price
    if(a>15):
        return price
    math_test(price*0.1+price,a)


math_test(50000,0)