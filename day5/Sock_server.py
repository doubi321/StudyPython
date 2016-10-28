#! /usr/bin/env python
#encoding=utf-8
## By written wangzai 2016-10-26
####单线程模式

import socket

HOST,PORT = '192.168.1.99',9000      ##设置ip和端口
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  ## 定义socket类型以及socket数据报格式（socket.SOCK_STREAM for TCP,
s.bind((HOST,PORT))			##绑定端口				## socket.SOCK_DGRAM for UDP)
s.listen(1)                      ## 同时接受1个链接

while True:
    conn,addr = s.accept()           ## 每一个客户端只要连过来，accept()方法就会返回2个结果，conn为实例，addr为地址ip
    print 'Connected by',addr
    while True:
        data = conn.recv(1024)      ## 接受客户端发过来的消息
        if not data:break
        conn.sendall(data.upper())         ## 把客户端的消息返回去 
        print "Received:",data

conn.close()
