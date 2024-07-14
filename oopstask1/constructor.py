class Students:
    Name=None
    Sub1=None
    Sub2=None
    Sub3=None
    Sub4=None
    Sub5=None
    def __init__(self,name,sub1,sub2,sub3,sub4,sub5):
        self.Name=name
        self.Sub1=sub1
        self.Sub2=sub2
        self.Sub3=sub3
        self.Sub4=sub4
        self.Sub5=sub5
    def tot(self):
        print(self.Name ,"=>" , "Total is",(self.Sub1+self.Sub2+self.Sub3+self.Sub4+self.Sub5))
        
stu1=Students("Narayanan",23,23,23,23,23) 
Students.tot(stu1)