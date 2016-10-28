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
    cur.execute('select count(*) from uc_user')
    result = cur.fetchall()
    print result[0][0]
    cur.execute('select version()')
    data = cur.fetchone()
    print "Databases version: %s " %  data
    cur.close()
    conn.close()

except MySQLdb.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])


