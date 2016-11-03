#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib2  
import os
num=0

if(os.path.exists('/home/python/stock2.txt')):
    os.remove('/home/python/stock2.txt')    
elif(os.path.exists('/home/python/stock2.txt')):
    f=open('/home/python/stock2.txt','w')    


for i in range(1,3000):  
    cl = 'http://hq.sinajs.cn/list=sz'
    c= "%d" %i;
    s = c.zfill(6)
    url = '%s%s' %(cl,s)

    #url='http://hq.sinajs.cn/list=sz000034'
    page = urllib2.urlopen(url) 
    print "%s" %(url)
    if i ==2752  :
        continue 
    stock_data = page.read().split('"')[1]
    name = stock_data.split(',')[0]
    name = name.decode('gb2312').encode('utf-8')
 
    if name == '':
        continue   
    

    open_price = float(stock_data.split(',')[1])
    last_closed_price = float(stock_data.split(',')[2])
    now_price = float(stock_data.split(',')[3])
    high_price= float(stock_data.split(',')[4])
    low_price= float(stock_data.split(',')[5])
    zhangfu=float((now_price - last_closed_price ) * 100 / last_closed_price)
    if zhangfu > 9.8: 
        print "%s,%s,今天开盘价：%5.2f ,目前价：%5.2f,昨天收盘价：%5.2f,涨幅：%4.2f%%" %(s,name,open_price,now_price,last_closed_price,zhangfu)
        num=num+1
            #print "%s,今天开盘价：%s ,目前价位：%s,昨天收盘价：%s,涨幅：%9.2f%%" %(name,open_price,now_price,last_closed_price,zhangfu) 
        f = open("/home/python/stock2.txt", 'a')    
        print >> f, "%s,%5.2f ,%5.2f,%5.2f,涨幅：%s%%" %(s,open_price,now_price,last_closed_price,zhangfu)
   
print "今天中小板涨停的股票数目  %d" %(num) 
   




