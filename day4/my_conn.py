#! /usr/bin/env python

import MySQLdb
try:
    conn=MySQLdb.connect(host='127.0.0.1',user='root',db='uooc',port=3306)
    cur=conn.cursor()
    cur.execute('select id,name,email from uc_user where id<20')
    result = cur.fetchall() 
    for record in result:
	print record
    cur.execute('select version()')
    data = cur.fetchone()
    print "Databases version: %s " %  data
    cur.close()
    conn.close()
except MySQLdb.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])
