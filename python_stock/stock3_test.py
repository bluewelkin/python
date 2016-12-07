#!/usr/bin/env python
# -*- coding:utf-8 -*-

#创业板 股票 涨停的票
import urllib2  
import os
num=0



for i in range(300000,302000):  
    cl = 'http://hq.sinajs.cn/list=sz'
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
        #print "%d,今天开盘价：%5.2f ,目前价：%5.2f,昨天收盘价：%5.2f,涨幅：%4.2f%%" %(i,opening_price,now_price,last_day_closed_price,zhangfu)
        #num=num+1
            #print "%s,今天开盘价：%s ,目前价位：%s,昨天收盘价：%s,涨幅：%9.2f%%" %(name,opening_price,now_price,last_day_closed_price,zhangfu) 
        #f = open("./stock3.txt", 'a')    
        #print >> f, "%d,%5.2f ,%5.2f,%5.2f,涨幅：%4.2f%%" %(i,opening_price,now_price,last_day_closed_price,zhangfu)
        print name
        value=[i,name,opening_price,last_day_closed_price,now_price]
        #value=value.decode('gb2312').encode('utf-8')
        print value

print "今天创业板涨停的股票数目  %d" %(num) 
   
