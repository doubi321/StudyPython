

class Dog:
    
    favorate_food = 'bone'
    #self.FavorFood = favorate_food
    def sayHi(self):
    	print 'Hi master , I am your little dog, who do you wnat me to bite...'
    def eat(self, food_type):
	if food_type == 'bone':
		print 'I like it very much..thanks'
	#else:
	#	print 'Do not give me this bull shit...'

d = Dog()
d.sayHi()
d.eat('bone')
