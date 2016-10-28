#! /usr/bin/env python
# encoding=utf-8

import time
import os
import datetime
import MySQLdb

#mon = 'log_' + time.strftime('%Y%m')
#day = time.strftime('%Y-%m-%d')

## 获取昨天的年月日
now_time = datetime.datetime.now()
yes_time = now_time + datetime.timedelta(days=-4)
mon = 'log_' + yes_time.strftime('%Y%m')
day = yes_time.strftime('%Y-%m-%d') + '%'
print type(mon),type(day)
try:
    conn=MySQLdb.connect(host='127.0.0.1',user='root',db='uooc',port=3306,charset='utf8')
    cur=conn.cursor()
    cur.execute('select id,name from uc_user limit 20')
    result = cur.fetchall()
    for record in result:
	if len(str(record[0])) < 3:
	    print str(record[0]) + '   ' + record[1]
	else:
	    print record[0],record[1]
    cur.execute('select version()')
    data = cur.fetchone()
    print "Databases version: %s " %  data
    cur.close()
    conn.close()

    conn = MySQLdb.connect(host='127.0.0.1',user='root',db='uc_action_log',port=3306)
    cur = conn.cursor()
    cur.execute('select count(distinct uid) from %s where time like "%s"' % (mon,day))
    sum = cur.fetchall()
    print 'UV: ' + str(sum[0][0])
    cur.close()
    conn.close()

except MySQLdb.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])


