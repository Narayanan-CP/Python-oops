# this is called single level inheritance
        
#  this is called as parent class       
class Parent:
    def __init__(self):
        self.networth=100000
    def swim(self,speed):
        print("parents is swimming",speed) 
        
#  this is called as child class       
class Child(Parent):
    def drive(self,speed):
        print("Child is driving",speed)
         
         
child1=Child()
parent1=Parent()
# child1.?(20)
print(child1.networth)


         
         
                      