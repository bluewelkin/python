#!/usr/bin/env python
# -*- coding:utf-8 -*-

#数据库的id要注意，因为002205之类的前面0，都修改为s，字符串存储

import urllib2  
import os
import MySQLdb
num=0

if(os.path.exists('F:/workspace/pythontest/src/stock2.txt')):
    os.remove('F:/workspace/pythontest/src/stock2.txt')    
elif(os.path.exists('F:/workspace/pythontest/src/stock2.txt')):
    f=open('stock2.txt','w')    


for i in range(1,3000):  
    cl = 'http://hq.sinajs.cn/list=sz'
    c= "%d" %i;
    s = c.zfill(6)
    
    print s;
    url = '%s%s' %(cl,s)

    #url='http://hq.sinajs.cn/list=sz000034'
    page = urllib2.urlopen(url) 
    #print "%s" %(url)
    if i ==2752  :
        continue 
    stock_data = page.read().split('"')[1]
    name = stock_data.split(',')[0]
    #name = name.decode('gb2312').encode('utf-8')
 
    if name == '':
        continue   
    

    open_price = float(stock_data.split(',')[1])
    last_closed_price = float(stock_data.split(',')[2])
    now_price = float(stock_data.split(',')[3])
    high_price= float(stock_data.split(',')[4])
    low_price= float(stock_data.split(',')[5])
    deal_gupiao=float(stock_data.split(',')[8]) #成交的股票数，由于股票交易以一百股为基本单位，所以在使用时，通常把该值除以一百；
    deal_gupiao=deal_gupiao/100
    deal_gupiao=int(deal_gupiao)
    deal_jine=float(stock_data.split(',')[9]) #成交金额，单位为“元”，为了一目了然，通常以“万元”为成交金额的单位，所以通常把该值除以一万；
    deal_jine=deal_jine/10000
    deal_jine=int(deal_jine)
    riqi=stock_data.split(',')[30]
    riqi=riqi.replace('-','')
    time=stock_data.split(',')[31]
    time=time.replace(':','')
    time=time[:-2]
    zhangfu=float((now_price - last_closed_price ) * 100 / last_closed_price)
    zhangfu= round(zhangfu,2)
    
        #connect_mysql_storage_data()
    conn=MySQLdb.connect(host='localhost',user='root',passwd='admin',port=3306,charset="utf8") 
    cur=conn.cursor()       
    #cur.execute('create database if not exists python') 
    conn.select_db('python')          
    name = name.decode('gb2312').encode('utf-8')           
    name2= '"%s"' % name
    s ='"%s"' % s
   # cur.execute("insert into stock values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" \
     #           %(i,name2,open_price,last_closed_price,now_price,high_price,low_price,deal_gupiao,deal_jine,riqi,time))
    table_name='%s%s' %('stock2',riqi)
    #print i
    
    if i==000001:    
       cur.execute("create table %s (id varchar(10) PRIMARY KEY,name varchar(20),zhangfu FLOAT(5,2),\
       open_price varchar(10),last_closed_price varchar(10),now_price varchar(10),\
       high_price varchar(10),low_price varchar(10),deal_gupiao int(20),\
       deal_jine int(20),riqi date,time time) ENGINE=InnoDB DEFAULT CHARSET=utf8;" %(table_name))
    print s
    cur.execute("insert into %s values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"  %(table_name,s,name2,zhangfu,open_price,last_closed_price,now_price,high_price,low_price,deal_gupiao,deal_jine,riqi,time))
    conn.commit() 
    cur.close() 
    conn.close()

    if zhangfu > 9.8:
        print "%s,今天开盘价：%5.2f ,目前价：%5.2f,昨天收盘价：%5.2f,涨幅：%4.2f%%" %(s,open_price,now_price,last_closed_price,zhangfu)
        num=num+1
            #print "%s,今天开盘价：%s ,目前价位：%s,昨天收盘价：%s,涨幅：%9.2f%%" %(name,open_price,now_price,last_closed_price,zhangfu) 
        f = open("./stock2.txt", 'a')    
        print >> f, "%d,%5.2f ,%5.2f,%5.2f,涨幅：%s%%" %(i,open_price,now_price,last_closed_price,zhangfu)
   
print "今天中小板涨停的股票数目  %d" %(num) 
   



