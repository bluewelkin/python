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
    
    message = MIMEText('��ַ�򲻿������� ��־', 'plain', 'utf-8')
    message['From'] = Header("url check", 'utf-8')
    message['To'] =  Header("url check", 'utf-8')
    
    subject = '%s �򲻿������� ��־' %url_doce
    message['Subject'] = Header(subject, 'utf-8')
    try:
        smtpObj = smtplib.SMTP() 
        smtpObj.connect(mail_host, 25)  
        smtpObj.login(mail_user,mail_pass)  
        smtpObj.sendmail(sender, receivers, message.as_string())
        print "%s �򲻿������� ��־ "%url_doce
    except smtplib.SMTPException:
        print "Error: �޷������ʼ�"
def code_url():
    for i in code_list:
        req = Request(i)  
        try:    
            response = urlopen(req)
            print "[�ɹ�] | URL:%s"%i
        except URLError,e:
            error = '[ʧ��] | URL:%sʧ��; URLErrorʧ����Ϣ:%s\n'%(i,e)
            mail_warin()
            print error
            with open(fname,'a')  as f:
                f.write(error)
            continue
        except  HTTPError,e:
            error = '[ʧ��] | URL:%sʧ��; HTTPErrorʧ����Ϣ:%s\n'%(i,e)
            mail_warin()
            print error
            with open(fname,'a')  as f:
                f.write(error)
            continue
        except Exception, e:
            error = '[ʧ��] | URL:%sʧ��; Exceptionʧ����Ϣ:%s\n'%(i,e)
            mail_warin()
            print error
            with open(fname,'a')  as f:
                f.write(error)
            continue
   # f.close

print "���ڿ�ʼִ��,��д���ļ�[%s]"%fname
code_url()