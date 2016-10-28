
#! /usr/bin/env python

import sys
import cPickle as p

shoplistfile = 'User_login.txt'
shoplist = [['wangzai','123456',1],['doubi','111111',2]]
f=file(shoplistfile,'w')
p.dump(shoplist,f)
f.close()

#print shoplist
locked = 1
retry_counter = 0
i = 0
while retry_counter < 3:
    user = raw_input('Username:').strip()
    if len(user) == 0:
	    print '\033[31;1mUsername cannot be empty! \033[0m'
	    continue
    while True:
        passwd = raw_input('Password:').strip()
        if len(passwd) == 0:
            print '\033[31;1mPassword cannot be empty! \033[0m'
	    continue
   	else:
	    break

    #handle the username and passwd empty issue

    # going to the loging verification part

    for i in (0,len(shoplist)-1):
	#print "11=",shoplist[i][2],shoplist[i]
        if shoplist[i][2] >= 3: #means the user is locked
	    print 'Your username is locked!'
	    sys.exit()
        elif  user == shoplist[i][0]  and passwd == shoplist[i][1]:
	    #means passwd the verfification
	    print "your = ",shoplist[i],shoplist[i][2]
	    sys.exit('Welcome %s login to our system!' % user)
    
    retry_counter += 1
    shoplist[i][2] += 1
    print shoplist[i][2]
    print '\033[31;1mWrong username or password,you have %s more chances!\033[0m' % (3 - retry_counter)

	    
033.
