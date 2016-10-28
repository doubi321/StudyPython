#! /usr/bin/env python

#def sayHI(*args):
#    print args

#sayHI('Alex',24,'SA','Chendoubi')

def sayHI2(**kargs):
    print kargs
    if kargs.has_key('name'):
	print kargs['name']
    
#name_list = {
#    'name':'wangzai',
#    'age':24,
#    'phone':1111111
#}

sayHI2(name='Alex',age=24,phone=111111)
