#! /usr/bin/env python
#encoding=utf-8

## 使用ssh-keygen,复制本机公钥到目标机器上面，来连接远程机器

import paramiko
import sys,os

#username = 'www'
host = sys.argv[1]
username = sys.argv[2]
cmd = sys.argv[3]

s = paramiko.SSHClient()  #绑定实例
#s.load_system_host_keys() #加载本机HOST主机文件

s.set_missing_host_key_policy(paramiko.AutoAddPolicy())  ## 允许连接不在know_hosts文件中的主机
pkey_file = '/root/.ssh/id_rsa'
key = paramiko.RSAKey.from_private_key_file(pkey_file)
s.connect(host,22,username,pkey=key,timeout=5)  #连接远程主机
stdin,stdout,stderr = s.exec_command(cmd) #执行命令
cmd_result = stdout.read(),stderr.read() #读取命令结果

for line in cmd_result:
    print line,

s.close()
