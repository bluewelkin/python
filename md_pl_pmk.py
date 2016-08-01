#-*- coding: utf-8 -*-
#!/usr/bin/evn python
import paramiko
import threading
import os

def ssh2(ip,username,passwd,cmd):
	try:
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(ip,22,username,passwd,timeout=8)
		for m in cmd:
			stdin,stdout,stderr = ssh.exec_command(m)
			stdin.write("Y")   
			out = []
			for line in stdout.readlines():
				out.append(line.strip('\n'))


			print '%s\t"\033[1;32;40mSSH OK\033[0m"\t -exec "%s":'%(ip,m)
			for o in out:
					print o
		ssh.close()
	except :
		print '%s\t"\033[1;31;40mSSH Error\033[0m"\n'%(ip)

def sftp2(ip,username,passwd,mode,localpath,remotepath):
	try:
		ftp = paramiko.Transport((ip,22))
		ftp.connect(username=username,password=passwd)
		sftp = paramiko.SFTPClient.from_transport(ftp)
		if mode.strip().upper()=='PUT':
			sftp.put(localpath,remotepath)
			print '%s\t"\033[1;32;40mFTP Upload OK\033[0m"\n'%(ip)
		elif mode.strip().upper()=='GET':
			sftp.get(remotepath,localpath)
			print '%s\t"\033[1;32;40mFTP Download OK\033[0m"\n'%(ip)
		else:
			print '%s\t"\033[1;31;40mPlease Input PUT or GET\033[0m"\n'%(ip)
		ftp.close()
	except :
		print '%s\t"\033[1;31;40mFTP Error\033[0m"\n'%(ip)


if __name__=='__main__':
        username = "bmviewer"  #用户名
        passwd = "BMP@+@w%t*i016"    #密码
	threads = [4]   #多线程
	iplist = []
        f = open('./iplist','r')
	while True:
		line = f.readline()
		if line:
			iplist.append(line.strip())
		else:
			break
	print "exec list:",iplist
	f.close()		
	print "Begin......"
	model = raw_input("Enter your input SSH/FTP: ") 
	if model.strip().upper() == "SSH":
		input = raw_input("Enter your input CMD: ")
		cmd = input.strip().split(',')
		for ip in iplist:
			a=threading.Thread(target=ssh2,args=(ip,username,passwd,cmd))
			a.start()
	elif model.strip().upper() == "FTP":
		mode = raw_input("Enter your input PUT/GET: ")
		localpath = raw_input("Enter your input local: ")
		remotepath = raw_input("Enter your input remoto: ")		
		begin = time.time()
		for ip in iplist:
                        a=threading.Thread(target=sftp2,args=(ip,username,passwd,mode,localpath,remotepath))
			a.start()
	else:
		print "\033[1;31;40mInput Error: Please Input SSH or FTP\033[0m" 
		os._exit(1)
