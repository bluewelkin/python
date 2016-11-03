#!/usr/bin/env python
# -*- coding:utf-8 -*-
import urllib2  
num=0

for i in range(600000,604000):  
    cl = 'http://hq.sinajs.cn/list=sh'
    url = '%s%d' %(cl,i)
    #url='http://hq.sinajs.cn/list=sh601918'
    page = urllib2.urlopen(url)  
    

    stock_data = page.read().split('"')[1]
    name = stock_data.split(',')[0]
    name = name.decode('gb2312').encode('utf-8')
    if name == '':
        continue
    
    

    opening_price = float(stock_data.split(',')[1])
    last_day_closed_price = float(stock_data.split(',')[2])
    now_price = float(stock_data.split(',')[3])

    zhangfu=(now_price - last_day_closed_price ) * 100 / last_day_closed_price 
    if zhangfu > 9.8:
        print "%s,今天开盘价：%s ,目前价位：%s,昨天收盘价：%s,涨幅：%9.2f%%" %(name,opening_price,now_price,last_day_closed_price,zhangfu)
        num=num+1
    #print "%s,今天开盘价：%s ,目前价位：%s,昨天收盘价：%s,涨幅：%9.2f%%" %(name,opening_price,now_price,last_day_closed_price,zhangfu) 
print "今天涨停的股票数目  %d" %(num) 
   

