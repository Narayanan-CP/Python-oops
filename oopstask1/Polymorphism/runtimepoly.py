# to use runtime polymorphism we use inheritance
#with the help of method overriding only we can achieve run time polymorphism 
class Parent:
    def Drive(self):
        print("Parent is Driving")
class Child(Parent):
    def Drive(self):
        print("Child is driving") 
obj=None
name=input()
if name=="Parent":
    obj=Parent()
else:
    obj=Child()    
obj.Drive()
        
               
    