#!/usr/bin/python

import paramiko

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect("192.168.240.30",22,"bm", "seceret")

stdin, stdout, stderr = ssh.exec_command("free -m")

print stdout.readlines()

ssh.close()
