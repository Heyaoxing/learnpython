
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

url='https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gbk&word=%C5%ED%D3%DA%EA%CC&fr=ala&ala=1&alatpl=adress&pos=0&hs=2&xthttps=111111'
resp=urllib2.urlopen(url)
html=resp.read()

bs=BeautifulSoup(html)

print bs.select('.imgitem')