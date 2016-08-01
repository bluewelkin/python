#!/usr/bin/python
import paramiko

ip='192.168.240.30'
username='bmviewer'
passwd='secrert'
cmd='free -m'
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(ip,22,username,passwd,timeout=8)

stdin, stdout, stderr = ssh.exec_command(cmd)
stdin.write("Y")
out = []
for line in stdout.readlines():
        out.append(line.strip('\n'))
for o in out:
        print o
ssh.close()
