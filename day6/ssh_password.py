#! /usr/bin/env python
#encoding=utf-8

## 使用用户名密码连接远程机器

import paramiko
import sys,os

host = sys.argv[1]
user = 'www'
password = '123456'

cmd = sys.argv[2]

s = paramiko.SSHClient()  #绑定实例
s.load_system_host_keys() #加载本机HOST主机文件

s.set_missing_host_key_policy(paramiko.AutoAddPolicy())  ## 允许连接不在know_hosts文件中的主机
s.connect(host,22,user,password,timeout=5)  #连接远程主机
stdin,stdout,stderr = s.exec_command(cmd) #执行命令

cmd_result = stdout.read(),stderr.read() #读取命令结果

for line in cmd_result:
    print line,

s.close()
