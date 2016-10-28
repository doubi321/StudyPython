#/usr/bin/env python

class A:
  
    def __init__(self):
	self.name = 'wangzai'
	self.age = '25'
    def method(self):
#	print 'method print'
	pass

a = A()
print getattr(a,'name','not find')
print getattr(a,'age','not found')
#print getattr(a,'method','default')
print getattr(a,'method','wangzai')
