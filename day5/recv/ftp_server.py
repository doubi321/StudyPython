()
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
