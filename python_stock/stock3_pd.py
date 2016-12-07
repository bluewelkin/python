#!/usr/bin/env python
# -*- coding:utf-8 -*-

#创业板判断
import urllib2 
file = open("stock3.txt") 
  
while 1: 
    line = file.readline() 
    if not line: 
        break
    else :
         #print "%s" %(line)
        i = line.split(',')[0] 
        cl = 'http://hq.sinajs.cn/list=sz'
        url = '%s%s' %(cl,i)
        #print url
    #url='http://hq.sinajs.cn/list=sh601918'
        page = urllib2.urlopen(url) 
        stock_data = page.read().split('"')[1]
        name = stock_data.split(',')[0]
    #name = name.decode('gb2312').encode('utf-8')
        open_price = float(stock_data.split(',')[1])
        last_closed_price = float(stock_data.split(',')[2])
        now_price = float(stock_data.split(',')[3])    
       
        if open_price > last_closed_price and now_price <= last_closed_price :
            print "要一字板强势，洗盘动作才入，至少要2点钟之前的一字板 %s" %(i)
         
  

   
        

   
