#/usr/bin/env python
#coding:utf-8
import sys
import cPickle as p
staff_dic = {}

f = file('credit.txt')
for line in f.xreadlines():
    cre_no,cre_pwd,bank,credit = line.split()
    staff_dic[cre_no] = [cre_pwd,bank,credit]


print staff_dic
	
while True:
    
    query = raw_input('\033[32;1mPlease input the query string:\033[0m').strip()
    if query == 'quit':
	print "You have pulled out of the system."
     	sys.exit('Goodbye!')
    if len(query) == 0:
 	continue
   
    match_counter = 0
    
    for k,v in staff_dic.items():
	index = k.find(query)
	if index != -1:
	    print k[:index] + '\033[32;1m%s\033[0m' % query + k[index + len(query):],v
	    match_counter += 1
			
	else:
	    str_v = '\t'.join(v)
	    index = str_v.find(query)
	    if index != -1:
	        print k,str_v[:index] + '\033[32;1m%s\033[0m' % query + str_v[index + len(query):]
		match_counter +=1
    print "The record is %s." % match_counter	
