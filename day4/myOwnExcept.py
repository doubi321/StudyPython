

class AlexException(Exception):
	pass 
	#def __init__(self,err):
	#	self.err = err	
	#def __str__(self):
	#   return 'Input info is wrong... %s' %self.err
try: 
	name = raw_input('Name:').strip()
	if name != 'alex': 
		raise AlexException(name)
except AlexException,e:
	print 'No valid name sepecfied...',e
