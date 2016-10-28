#! /usr/bin/env python
#encoding=utf-8
## By written wangzai 2016-10-26

import socket

host,port = '192.168.1.99',9000
c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect((host,port))

#c.send('Hello world!!!')
#return_data = c.recv(1024)      ##收回数据
#print 'Received:',return_data
def recv_all(obj,msg_length):
    raw_result = ''
    while msg_length !=0:
        if msg_length <= 4096:
            data = obj.recv(msg_length)
            msg_length = 0
        else:
            data = obj.recv(4096)
            msg_length -= 4096

        raw_result += data
    return raw_result

while True:
    user_input = raw_input("msg to send::").strip()
    if len(user_input) == 0:continue
    c.send(user_input)
 
    recv_size = int(c.recv(1024))
    #recv_data = c.recv(int(recv_size))
    print 'data size from server',int(recv_size)

    result = recv_all(c,recv_size)
    print result

c.close()

