#!/usr/bin/env python
# -*- coding:utf-8 -*-

#创业板 股票 涨停的票 存入数据库
import urllib2  
import MySQLdb 
num=0
for i in range(300000,302000):  
    cl = 'http://hq.sinajs.cn/list=sz'
    url = '%s%d' %(cl,i)
    #url='http://hq.sinajs.cn/list=sh601918'
    page = urllib2.urlopen(url) 
    stock_data = page.read().split('"')[1]
    name = stock_data.split(',')[0]
    #name = name.decode('gb2312').encode('utf-8')
    if name == '':
        continue     

    opening_price = float(stock_data.split(',')[1])
    last_day_closed_price = float(stock_data.split(',')[2])
    now_price = float(stock_data.split(',')[3])

    zhangfu=(now_price - last_day_closed_price ) * 100 / last_day_closed_price 
    if zhangfu > 9.8:
        print "%d,今天开盘价：%5.2f ,目前价：%5.2f,昨天收盘价：%5.2f,涨幅：%4.2f%%" %(i,opening_price,now_price,last_day_closed_price,zhangfu)
        num=num+1
            #print "%s,今天开盘价：%s ,目前价位：%s,昨天收盘价：%s,涨幅：%9.2f%%" %(name,opening_price,now_price,last_day_closed_price,zhangfu) 
        f = open("./stock3.txt", 'a')    
        print >> f, "%d,%5.2f ,%5.2f,%5.2f,涨幅：%4.2f%%" %(i,opening_price,now_price,last_day_closed_price,zhangfu)
        try: 
            conn=MySQLdb.connect(host='localhost',user='root',passwd='admin',port=3306,charset="utf8") 
            cur=conn.cursor() 
      
            #cur.execute('create database if not exists python') 
            conn.select_db('python') 
            #cur.execute('create table stock(id varchar(10) PRIMARY KEY,name varchar(10),opening_price varchar(10),last_day_closed_price varchar(10),now_price varchar(10))') 
      
            
            #cur.execute('insert into stock values(%s,%s,%s,%s,%s),i,name,opening_price,last_day_closed_price,now_price') 
            #print value
          
            #value = [i,name,opening_price,last_day_closed_price,now_price]
            #print value           
            #cur.execute('insert into stock values(%s,%s,%s,%s,%s)',value) 
            name = name.decode('gb2312').encode('utf-8')    
           
            name2= '"%s"' % name
            #print "insert into stock values(%s,%s,%s,%s,%s)" %(i,name2,opening_price,last_day_closed_price,now_price)
               
            #print name2
            #cur.execute("insert into stock(i,name,opening_price,last_day_closed_price,now_price) values(%s,%s,%s,%s,%s)"%(i,name,opening_price,last_day_closed_price,now_price))
            #print "insert into stock values(%s,%s,%s,%s,%s)" %(i,name2,opening_price,last_day_closed_price,now_price)
            cur.execute("insert into stock values(%s,%s,%s,%s,%s)" %(i,name2,opening_price,last_day_closed_price,now_price))
            cur.execute( "update stock set stock.name=%s where id=%s" %(name2,i))
            
            #print "update stock set stock.name=%s where id=%s" %(name2,i)
           
            #print "values(%s,%s,%s,%s,%s)" %(i,name,opening_price,last_day_closed_price,now_price)
            
            conn.commit() 
            cur.close() 
            conn.close() 
        except MySQLdb.Error,e: 
            print "Mysql Error %d: %s" % (e.args[0], e.args[1]) 
        #insert into stock values(300021,"大于", 14.73, 14.85, 16.34);
         #create table stock(id varchar(10) PRIMARY KEY,name varchar(20),opening_price varchar(10),last_day_closed_price varchar(10),now_price varchar(10)) ENGINE=InnoDB DEFAULT CHARSET=utf8;
 #drop tables stock;
 #drop database python;
  #update stock set stock.name='好' where id = 300498;
#create table stock (id varchar(10) PRIMARY KEY,name varchar(20)
#mysql> create table stock (id varchar(10) PRIMARY KEY,name varchar(20),opening_p
#rice varchar(10),last_day_closed_price varchar(10),now_price varchar(10),high_pr
#ice varchar(10),low_price varchar(10),deal_gupiao varchar(20),deal_jine varchar(
#20),riqi date,time varchar(20)) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#create database python;
print "今天创业板涨停的股票数目  %d" %(num) 
   
