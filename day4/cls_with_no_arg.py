
class person:

    def tell(self,name):
        print 'hi my name is ', name
        
    def study(self):
        print 'I am stuying Py right now'    
        
class student(person):
    
    def study(self):
        print 'I am stuying Py right now'       

p = person()
vars = ['tell', 'study']
v1 = vars[0]
getattr(p, v1)('Oldboy')
getattr(p,'tell')('wangzai')
getattr(p,'study')()






