#! /usr/bin/env python
#encoding=utf-8
## 多线程，阻塞方式

import SocketServer

class MySockServer(SocketServer.BaseRequestHandler):

    def handle(self):
        print 'Got a new conn from',self.client_address
        while True:
            data = self.request.recv(1024)
	    if not data:
		print 'Lost connection with',self.client_address
		break
            print 'received:',data
            self.request.sendall(data.upper())

if __name__ == '__main__':
    h ='192.168.1.99'
    p = 9000
    s = SocketServer.ThreadingTCPServer((h,p),MySockServer)
    s.serve_forever()

