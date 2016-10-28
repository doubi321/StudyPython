
try: 
	name = ['a','b','c']
	name[5]
	info_dic = {}
	name = raw_input('Name:').strip()
	age = raw_input('Age:').strip()
	if len(name) ==0:
		raise KeyError
except ValueError:
	print 'value err'
except:
	print 'err happend... '

