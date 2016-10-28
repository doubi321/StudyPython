#! /usr/bin/env python

class person:
   
    blood = 0
    attract = 0
    school_name = None
    skills = []
    love_status = None
    lover = None
    job = None
    company = None
    #skill = None

    def __init__(self,name,sex,role):
	self.name = name
	self.sex = sex
	self.role = role
	print '\033[32;1m-\033[0m'*60
	
	if self.role == 'assassinator':
	    self.blood += 2000
	    self.attract += 400
       	    print '\033[31;1mMy name is %s,I am a %s,I have %s blood and %s attract to kill everyone.\033[0m' %(self.name,self.role,self.blood,self.attract)

  	elif self.role == 'tank':
            self.blood += 4000
            self.attract += 120
            print '\033[31;1mMy name is %s,I am a %s,I have %s blood and %s attract to killed by everyone.\033[0m' %(self.name,self.role,self.blood,self.attract)

	elif self.role == 'ad':
            self.blood += 1800
            self.attract += 500
            print '\033[31;1mMy name is %s,I am a %s,I have %s blood and %s attract,I can avoid a lot of damage.\033[0m' %(self.name,self.role,self.blood,self.attract)

    def Blood(self,skill):
	if skill == 'A':
	    self.blood -= 500
	#    print '\033[31;1mI am is %s,I was %s %s skill attack,only %s of the blood and so sad.\033[0m' %(self.name,self.lover,skill,self.blood)

	if skill == 'R':
            self.blood -= 1500
        print '\033[31;1mI am is %s,I was %s %s skill attack,only %s of the blood and so sad.\033[0m' %(self.name,self.lover,skill,self.blood)

    def Study(self,school):
	if school == 'aming linux':
	    self.attract += 200
	    skill = 'linux'
	elif school == 'oldboy':
	    self.attract += 300
	    skill = 'python'
	return(school,skill)

    def Job(self,company):
	if company == '360':
	    if self.attract >= 300:
		position = 'yunwei'
	    if self.attract >=400:
		position = 'yunwei developer'
	elif company == 'tencent':
	    if self.attract >= 350:
                position = 'yunwei'
            if self.attract >=500:
                position = 'yunwei developer'
 	print '\033[31;1mHi,my name is %s,my current attract is %s,my company is %s, my position is %s.\033[0m' %(self.name,self.attract,company,position)	
    

p1 = person('xiaoyuren','man','assassinator')
p2 = person('dema','man','tank')
p3 = person('ad','famale','ad')

p2.lover = p1.name
p2.Blood('A')
p2.Blood('R')	

school_name,skills = p2.Study('oldboy')
p2.school_name = school_name
p2.skills.append(skills)
print 'Now %s has skills %s from the %s ,going to do the interview in 360' %(p2.name,p2.skills,p2.school_name)

p2.Job('360')
p2.Job('tencent')


