#!/usr/bin/env python
# -*- coding:utf-8 -*-

#上证指数 大盘分析报告
#1、波浪理论 上涨过程12345浪，下跌过程ABC浪→对应的买点 123 卖点4 和卖点123和买点4----趋势
#2、11天理论  经过一段时间的上证，大盘要回调休息了，到第10天就要小心了
#3、操作来操作去，还不如买一两只票满仓干-----而下跌过程则可以分散多只票，但大盘下跌，每个票的点数都是一样的。
#4、买股票不能看感觉
#5、遇到季线60天线要回调 如2015-10-21
#6、5天线、10天线黄金交叉要回调
#7、30分钟kd向下带动60分钟kd向下，带动日Kd向下-------就要开始动作。跟着信号上车，跟着信号下车。 2015年10月21日
#8、不要凭感觉做交易。 ---------永远的

import urllib2  
url='http://hq.sinajs.cn/list=sh000001'
page = urllib2.urlopen(url) 

 
stock_data = page.read().split('"')[1]
name = stock_data.split(',')[0]
name = name.decode('gb2312').encode('utf-8')
 

    

opening_price = float(stock_data.split(',')[1])
last_day_closed_price = float(stock_data.split(',')[2])
now_price = float(stock_data.split(',')[3])
stockZS =   float(stock_data.split(',')[8]) 
stockZS_W = float(stockZS / 100000000)  #手
stockJE =   float(stock_data.split(',')[9]) 
stockJE_Y   = str(int(stockJE) / 100000000)    #亿        
zhangfu=(now_price - last_day_closed_price ) * 100 / last_day_closed_price 
 
f = open("./stock_001.txt", 'a')    
print ('上证指数分析报告:开盘指数 %s,昨天收盘指数 %s，目前指数 %s 涨幅%4.2f%% 成交手 %4.2f亿手  成交金额  %s亿')  %(opening_price,last_day_closed_price,now_price,zhangfu,stockZS_W,stockJE_Y )



url5='http://hq.sinajs.cn/list=sz399005'
page = urllib2.urlopen(url5) 

 
stock_data = page.read().split('"')[1]
name = stock_data.split(',')[0]
name = name.decode('gb2312').encode('utf-8')
 

    

opening_price = float(stock_data.split(',')[1])
last_day_closed_price = float(stock_data.split(',')[2])
now_price = float(stock_data.split(',')[3])
stockZS =   float(stock_data.split(',')[8]) 
stockZS_W = float(stockZS / 100000000)  #手
stockJE =   float(stock_data.split(',')[9]) 
stockJE_Y   = str(int(stockJE) / 100000000)    #亿        
zhangfu=(now_price - last_day_closed_price ) * 100 / last_day_closed_price 
 
f = open("./stock_002.txt", 'a')    
print ('中小创指分析报告:开盘指数 %s,昨天收盘指数 %s，目前指数 %s 涨幅%4.2f%% 成交手 %4.2f亿手  成交金额  %s亿')  %(opening_price,last_day_closed_price,now_price,zhangfu,stockZS_W,stockJE_Y )
   




url6='http://hq.sinajs.cn/list=sz399006'
page = urllib2.urlopen(url6) 

 
stock_data = page.read().split('"')[1]
name = stock_data.split(',')[0]
name = name.decode('gb2312').encode('utf-8')
 

    

opening_price = float(stock_data.split(',')[1])
last_day_closed_price = float(stock_data.split(',')[2])
now_price = float(stock_data.split(',')[3])
stockZS =   float(stock_data.split(',')[8]) 
stockZS_W = float(stockZS / 100000000)  #手
stockJE =   float(stock_data.split(',')[9]) 
stockJE_Y   = str(int(stockJE) / 100000000)    #亿        
zhangfu=(now_price - last_day_closed_price ) * 100 / last_day_closed_price 
 
f = open("./stock_003.txt", 'a')    
print ('创业板指分析报告:开盘指数 %s,昨天收盘指数 %s，目前指数 %s 涨幅%4.2f%% 成交手 %4.2f亿手  成交金额  %s亿')  %(opening_price,last_day_closed_price,now_price,zhangfu,stockZS_W,stockJE_Y )
   

url7='http://hq.sinajs.cn/list=sz399001'
page = urllib2.urlopen(url7) 

 
stock_data = page.read().split('"')[1]
name = stock_data.split(',')[0]
name = name.decode('gb2312').encode('utf-8')
 

    

opening_price = float(stock_data.split(',')[1])
last_day_closed_price = float(stock_data.split(',')[2])
now_price = float(stock_data.split(',')[3])
stockZS =   float(stock_data.split(',')[8]) 
stockZS_W = float(stockZS / 100000000)  #手
stockJE =   float(stock_data.split(',')[9]) 
stockJE_Y   = str(int(stockJE) / 100000000)    #亿        
zhangfu=(now_price - last_day_closed_price ) * 100 / last_day_closed_price 
 
f = open("./stock_004.txt", 'a')    
print ('深圳指数分析报告:开盘指数 %s,昨天收盘指数 %s，目前指数 %s 涨幅%4.2f%% 成交手 %4.2f亿手  成交金额  %s亿')  %(opening_price,last_day_closed_price,now_price,zhangfu,stockZS_W,stockJE_Y )
   



