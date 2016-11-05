#! /usr/bin/env python
#encoding=utf-8

## 使用用户名密码连接远程机器,上传(put)以及下载(get)文件

import paramiko
import sys,os

username = 'www'
password = '123456'
host = '192.168.1.210'

t = paramiko.Transport((host,22))
t.connect(username = username,password = password)
#pkey_file = '/root/.ssh/id_rsa'
#key = paramiko.RSAKey.from_private_key_file(pkey_file)
#t.connect(username,key)

sftp = paramiko.SFTPClient.from_transport(t)
sftp.get('/data/www/ucweb/config/application.ini','/tmp/app.ini')    ##get(原文件,目标文件)
sftp.put('/root/1.txt','/data/www/ucweb/1.txt')                      ##put(原文件,目标文件)

t.close()
