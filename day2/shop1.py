#! /usr/bin/env python
## By written wangzai 20160825

import sys

Salary = input('Please input your salary: ')

shoplist = [['Car',500000],['Iphone',5000],['Mac',2000],['Python',1000],['Time',50]]

while True:
    for p in shoplist:
  	print p[0],p[1]

    sth = raw_input('Please input you need to buy something: ')
    
    for i in range(len(shoplist)-1):
	Min = shoplist[0][1]
	if shoplist[i][1] < Min:
	    Min = shoplist[i][1] 
    
    if Salary < Min:
  	 print "Your not enough monery to buy everything."
	 sys.exit()

    for i in range(len(shoplist)-1):
    
        if sth == shoplist[i][0]:
	    if Salary >= shoplist[i][1]:
	   	 Salary = Salary - shoplist[i][1]
	   	 print "The %s alreadly in list." % shoplist[i][0]
	  	 print "You have %d money." % Salary
	  	 continue
	    else:
		print "You haven't enough monery to buy %s" % shoplist[i][0]
		continue
       # else:
       #	    print "The shoplist haven't this goods %d" % shoplist[i][0]
       #    continue
    
     
	
	    
