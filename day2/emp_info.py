#! /usr/bin/env python
#coding:utf-8
## By written wangzai 20160827

import sys

emp_info = [
    [111,'xiaochen','a@qq.com','market','spread','11111111'],
    [222,'xiaowang','b@qq.com','technology','IT','22222222'],
    [333,'xiaosong','c@qq.com','product','PM','33333333'],
    [444,'xiaomei','d@qq.com','technology','YW','44444444']
]

print '''
0--> 通过员工号查找.
1--> 通过名字查找(支持模糊查询).
quit--> 直接退出
'''
while True:
    num = raw_input("Please choice which method to find: ").strip()
    
    if num == 'quit':
	print "You have pulled out of the system."
     	sys.exit('Goodbye!')
    if len(num) == 0:
 	continue
    
    num = int(num)
    if num == 0:
	Empno = input("Please input employee number: ")
	for f in emp_info:
	    #print Empno,f[0]
	    if Empno == f[0]:
	        print emp_info[emp_info.index(f)]
		break
        else:
	    print "The Empno is not exist,please input again."
	    continue

    i = 0
    if num == 1:
	Empname = raw_input("Please input employee name or parted: ")
  	for f in emp_info:
	    if Empname in f[1]:
		print emp_info[emp_info.index(f)]
		i = i + 1
                continue
	print "The record is %d." % i












    
