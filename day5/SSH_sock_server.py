import SocketServer
import commands
import time

class MySockServer(SocketServer.BaseRequestHandler):

    def handle(self):
        print 'Got a new conn from',self.client_address
        while True:
            cmd = self.request.recv(1024)
            if not cmd:
                print 'Lost connection with',self.client_address
                break

            cmd_result = commands.getstatusoutput(cmd)
  	    self.request.send(str(len(cmd_result[1])))		
	    time.sleep(0.2)
            self.request.sendall(cmd_result[1])

if __name__ == '__main__':
    h ='192.168.1.99'
    p = 9000
    s = SocketServer.ThreadingTCPServer((h,p),MySockServer)
    s.serve_forever()
