class SchoolMember:
    school_name = 'Oldboy Linux edu.'
    def __init__(self, name, gender,nationality='CN'):
        self.name = name 
        self.gender = gender
        self.nation = nationality
    
    def tell(self):
        print 'Hi, my name is %s , I am from %s' %(self.name, self.nation)      

class Student(SchoolMember):
    
    def __init__(self,Name, Gender, Class , Score,Nation='US' ):
        SchoolMember.__init__(self,Name, Gender,Nation)
        self.Class = Class
        self.Score = Score
        #self.Name = name 
        
    def payTuition(self,amount):
        if amount < 6499:
            print 'Get the fuck off...'
        else:
            print 'Welcome onboard!'

class Teacher(SchoolMember):
    def __init__(self,Name, Gender, Course , Salary,Nation='FR'):
        SchoolMember.__init__(self,Name, Gender,Nation)
        self.Course = Course
        self.Salary = Salary 
        
        
    def teaching(self):
        print 'I am teaching %s, i am making %s per month !' %(self.Course, self.Salary)
        
        
S1 = Student('WangFanHao', 'Male', 'Python','C+','JP')
S1.tell()
S1.payTuition(4999)

S2 = Student('ShitTshirt', 'Male', 'Linux','B')
S2.tell()
S2.payTuition(6500)  

        
T1 = Teacher('Alex','Male', 'C++', 5000)
T1.tell()
T1.teaching()

#SchoolMember
            
        
