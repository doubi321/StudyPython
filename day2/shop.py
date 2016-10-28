#! /usr/bin/env python
## By written wangzai 20160825

import sys

Salary = input('Please input your salary: ')

shoplist = [
    ['Car',500000],
    ['Iphone',5000],
    ['Mac',2000],
    ['Python',1000],
    ['Time',50]
]

#create a shopping list
shopping_list = []

while True:
    for p in shoplist:                                   #print the shopping list and index.
        print shoplist.index(p),p[0],p[1]

    choice = raw_input('Please input you need to buy something(quit means end): ').strip()  
    if choice == 'quit':
	print "You have bought below stuff:"
	for i in shopping_list:
	    print '\t', i
	sys.exit('Goodbye!')
    elif len(choice) == 0:
	continue
    #if not choice.isdigit():                     
    elif choice.isalpha():                #if choice is words,and choice.isalpha() is True,choice.isdigit id False
	continue

    choice = int(choice)
    if choice >= len(shoplist):  #out of range
	print 'Could not find this item'
	continue 
    pro = shoplist[choice]
    if Salary >= pro[1]:                #means you can afford this
	Salary = Salary - pro[1]
	shopping_list.append(pro)
	print "Adding %s to shopping list,you have %s left." % (pro[0],Salary)
    else:
	print 'The price of %s is %s,yet your current balance is %s,so try another one!' % (pro[0],pro[1],Salary)

