
import time
def time_counter(func):
	def wrapper():
		start = time.time()
		func()
		end = time.time()
		print 'This fuunction costs :', end - start
	return wrapper
@time_counter
def tellYourSalary():
	print 'Allen makes 25K per month...'

#sayHi()

@time_counter
def sayHi():
        print 'hi your sister...'
        time.sleep(0.1)


sayHi()

tellYourSalary()
