class Students:
    Name=None
    Sub1=None
    Sub2=None
    Sub3=None
    Sub4=None
    Sub5=None
    def tot(self):
        print(self.Name ,"=>" , "Total is",(self.Sub1+self.Sub2+self.Sub3+self.Sub4+self.Sub5))
        
stu1=Students()
stu1.Name="Narayanan"
stu1.Sub1=23
stu1.Sub2=23
stu1.Sub3=23
stu1.Sub4=23
stu1.Sub5=23
stu1.tot()
        