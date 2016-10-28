#! /usr/bin/env python
#encoding=utf-8
## By written wangzai 2016-10-26

import socket
import os

host,port = '192.168.1.210',9000
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
    
    user_cmd = user_input.split()
    if user_cmd[0] == 'put':
	if len(user_cmd) == 2:
	    f = file(user_cmd[1],'rb')
	    f_size = os.stat(user_cmd[1]).st_size
	    c.send("%s %s %s" %(user_cmd[0],user_cmd[1],f_size))
	    
	    print 'going to send...'
	    c.sendall(f.read() )
	    print c.recv(1024)

#    elif user_cmd[0] == 'get':
#	if len(user_cmd) == 2:
	        
		    
c.close()
