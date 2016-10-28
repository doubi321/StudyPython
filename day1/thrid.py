#! /usr/bin/env python

name = raw_input('What is your name? :').strip()
if len(name) == 0:
    print 'Error: you must input sth as name.'
age = input('how old are you? :')
job = raw_input('What is your job?')

msg = '''
Information of %s as below:
    Name : \033[42;1m%s \033[0m
    Age  : %d
    job  : %s
''' % (name,name,age,job)

print type(age)
if age >= 30:
    print "You are too old,you can only work for..."
else:
    pass

print msg
