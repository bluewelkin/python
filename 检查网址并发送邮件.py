# -*- coding: UTF-8 -*-
#!/usr/bin/env python
###create by :ben huang

import smtplib
from email.mime.text import MIMEText
from email.header import Header
import commands,time

from urllib2 import Request, urlopen, URLError, HTTPError
fname = '/script/f_{0}.txt'.format(int(time.time()))
url_doce='https://xidi.bluemoon.com.cn/index'
code_list=['https://xidi.bluemoon.com.cn/index']

def mail_warin():
    mail_host="mail.bluemoon.com.cn"
    mail_user="aaa@bluemoon.com.cn" 
    mail_pass="111***zzz" 
    sender = 'aaa@bluemoon.com.cn'
    receivers = ['1@bluemoon.com.cn','2@bluemoon.com.cn','3@bluemoon.com.cn']
    
    message = MIMEText('网址打不开，请检查 日志', 'plain', 'utf-8')
    message['From'] = Header("url check", 'utf-8')
    message['To'] =  Header("url check", 'utf-8')
    
    subject = '%s 打不开，请检查 日志' %url_doce
    message['Subject'] = Header(subject, 'utf-8')
    try:
        smtpObj = smtplib.SMTP() 
        smtpObj.connect(mail_host, 25)  
        smtpObj.login(mail_user,mail_pass)  
        smtpObj.sendmail(sender, receivers, message.as_string())
        print "%s 打不开，请检查 日志 "%url_doce
    except smtplib.SMTPException:
        print "Error: 无法发送邮件"
def code_url():
    for i in code_list:
        req = Request(i)  
        try:    
            response = urlopen(req)
            print "[成功] | URL:%s"%i
        except URLError,e:
            error = '[失败] | URL:%s失败; URLError失败信息:%s\n'%(i,e)
            mail_warin()
            print error
            with open(fname,'a')  as f:
                f.write(error)
            continue
        except  HTTPError,e:
            error = '[失败] | URL:%s失败; HTTPError失败信息:%s\n'%(i,e)
            mail_warin()
            print error
            with open(fname,'a')  as f:
                f.write(error)
            continue
        except Exception, e:
            error = '[失败] | URL:%s失败; Exception失败信息:%s\n'%(i,e)
            mail_warin()
            print error
            with open(fname,'a')  as f:
                f.write(error)
            continue
   # f.close

print "现在开始执行,将写入文件[%s]"%fname
code_url()