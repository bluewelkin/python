#!/usr/bin/env python
# -*- coding:utf-8 -*-

#创业板 股票 涨停的票
import urllib2  
import os

if(os.path.exists('F:/workspace/pythontest/src/stock_yaogu.txt')):
    os.remove('F:/workspace/pythontest/src/stock_yaogu.txt')    
elif(os.path.exists('F:/workspace/pythontest/src/stock_yaogu.txt')):
    f=open('stock_yaogu.txt','w')  

ChinaStockIndividualList = [
    "000630", #  铜陵有色
    "002043", #  兔宝宝
    "300153", #  科泰电源
    "300191", #  潜能恒信
    "300329", #  海伦钢琴
    "000005", #  特力A
    "300431", #  暴风科技
    "000676", #  智度投资
    "600876", #  洛阳玻璃
    "002702", #  海欣食品
    "600680", #  上海普天
    "600868", #  梅雁吉祥
    "002424", #  贵州百灵
    "002506", #  协鑫集成
    "300092", #  科新机电
    "300262"  #  巴安水务
   
]
#国内股票数据：个股   
        
def test_china_individual_data():
    for stockCode in ChinaStockIndividualList:
        exchange = "sh" if (int(stockCode) // 100000 == 6) else "sz"
        dataUrl = "http://hq.sinajs.cn/list=" + exchange + stockCode        
        page = urllib2.urlopen(dataUrl)  
        stock_data = page.read().split('"')[1]
        name = stock_data.split(',')[0]
        name = name.decode('gb2312').encode('utf-8')
        opening_price = float(stock_data.split(',')[1])
        last_day_closed_price = float(stock_data.split(',')[2])
        now_price = float(stock_data.split(',')[3])
        zhangfu=(now_price - last_day_closed_price ) * 100 / last_day_closed_price 
        print ('%s,开盘价格 %s,昨天收盘价格 %s，目前价格 %s 涨幅%4.2f%%')  %(name,opening_price,last_day_closed_price,now_price,zhangfu)
        #if zhangfu > 9.8:     
            #print ('%s,开盘价格 %s,昨天收盘价格 %s，目前价格 %s 涨幅%4.2f%%')  %(name,opening_price,last_day_closed_price,now_price,zhangfu)   
            #f = open("./stock_yaogu.txt", 'a')    
            #print >> f, "%s,%5.2f ,%5.2f,%5.2f,涨幅：%4.2f%%" %(stockCode ,opening_price,now_price,last_day_closed_price,zhangfu)
   
 
def main():
    print "妖股"
    test_china_individual_data()
if __name__ == '__main__':
    main()
   
