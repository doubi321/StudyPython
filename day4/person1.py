#! /usr/bin/env python


class School:
    
    def __init__(self,name,gender,nation='China'):
	self.Name1 = name
	self.Gender1 = gender
	self.Nation1 = nation

    def tell(self):
	print ("Hi,my name is %s,and I am from %s" % (self.Name1,self.Nation1))

class Student(School):
    
    def __init__(self,Name,Gender,Class,Score,Nation='US'):
	School.__init__(self,Name,Gender,Nation)
	self.Class = Class
	self.Score = Score

    def wangzai(self,amount):
	if amount < 6499:
            print 'Get the fuck off...'
        else:
            print 'Welcome onboard!'

class Teacher(School):
    
    def __init__(self,Name,Gender,Course,Salary,Nation='Franch'):
	School.__init__(self,Name,Gender,Nation)
	self.Course = Course
	self.Salary = Salary

    def Teach(self):
	print 'I am teaching %s, i am making %s per month !' %(self.Course, self.Salary)


S1 = Student('wangzai', 'Male', 'Python','C+','JP')
S1.tell()
S1.wangzai(4999)

S2 = Student('doubi', 'Male', 'Linux','B')
S2.tell()
S2.wangzai(6500)  

        
T1 = Teacher('Alex','Male', 'C++', 5000)
T1.tell()
T1.Teach()

