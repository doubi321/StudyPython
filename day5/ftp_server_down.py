#! /usr/bin/env python
#encoding=utf-8
## By written wangzai 2016-12-27

## 模拟实现ftp账号远程登录通过获取数据

import SocketServer
import commands
import time
import re

class MySockServer(SocketServer.BaseRequestHandler):
    
    def recv_all(self,obj,msg_length,des_file):
    #raw_result = ''
        while msg_length !=0:
            if msg_length <= 4096:
                data = obj.recv(msg_length)
                msg_length = 0
		print 'to less',msg_length
            else:
                data = obj.recv(4096)
                msg_length -= 4096

     #   raw_result += data
    #return raw_result    
	    des_file.write(data)
        return 'Done'

    def handle(self):
        print 'Got a new conn from',self.client_address
        
	while True:
            cmd = self.request.recv(1024)
            if not cmd:
                print 'Lost connection with',self.client_address
                break

	 #   option,filename,file_size = cmd.split()
	    cmd_c = cmd.split()
	    if cmd_c[0] == 'put':
		# client wants to upload file
		file_size = re.sub('\D','',cmd_c[2])
		print int(file_size)
		f = file('recv/%s' % cmd_c[1],'wb')
		write_to_file = self.recv_all(self.request,int(file_size),f)
		if write_to_file == 'Done':
		    self.request.send('File uploaded success')
		    f.close()
  	    else:
		print 'start send cmd back info.'
		cmd_result = commands.getstatusoutput(cmd_c[0])
		self.request.send(str(len(cmd_result[1])))
		self.request.sendall(cmd_result[1])

if __name__ == '__main__':
    h ='192.168.1.99'
    p = 9000
    s = SocketServer.ThreadingTCPServer((h,p),MySockServer)
    s.serve_forever()
