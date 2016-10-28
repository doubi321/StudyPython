

class Dog:
  
  def sayHi(self):
    	print 'Hi master , I am your little dog, who do you wnat me to bite...'
    	favorate_food = 'bone'
    	self.FavorFood = favorate_food
  def eat(self, food_type):
	if food_type == self.FavorFood:
		print 'I like it very much..thanks'
	else:
		print 'Do not give me this bull shit...'

d = Dog()
d.sayHi()
d.eat('bone')
