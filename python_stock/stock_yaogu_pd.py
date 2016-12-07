#!/usr/bin/env python
# -*- coding:utf-8 -*-

#创业板 股票 涨停的票
import urllib2  
import os
#国内股票数据：个股   
        
def test_china_individual_data():
    file = open("stock_yaogu.txt")  
    while 1: 
        line = file.readline() 
        if not line: 
            break
        else :
           #print "%s" %(line)
            stockCode = line.split(',')[0]        
            exchange = "sh" if (int(stockCode) // 100000 == 6) else "sz"
            dataUrl = "http://hq.sinajs.cn/list=" + exchange + stockCode        
            page = urllib2.urlopen(dataUrl)  
            stock_data = page.read().split('"')[1]
            name = stock_data.split(',')[0]
            name = name.decode('gb2312').encode('utf-8')
            opening_price = float(stock_data.split(',')[1])
            last_day_closed_price = float(stock_data.split(',')[2])
            zhangtijia=last_day_closed_price *1.1
            now_price = float(stock_data.split(',')[3])
            zhangfu=(now_price - last_day_closed_price ) * 100 / last_day_closed_price 
            #print ('%s,开盘价格 %s,昨天收盘价格 %s，目前价格 %s 涨幅%4.2f%%')  %(name,opening_price,last_day_closed_price,now_price,zhangfu)
            if now_price <= last_day_closed_price :    
                print ('洗盘的入 %s,开盘价格 %s,昨天收盘价格 %s，目前价格 %s 涨幅%4.2f%%')  %(name,opening_price,last_day_closed_price,now_price,zhangfu)   
            if now_price <= zhangtijia :    
                print ('没有封板 %s,开盘价格 %s,昨天收盘价格 %s，目前价格 %s 涨幅%4.2f%%')  %(name,opening_price,last_day_closed_price,now_price,zhangfu)   
        
 
def main():
    print "妖股洗盘和未封板的票 "
    test_china_individual_data()
if __name__ == '__main__':
    main()
   
