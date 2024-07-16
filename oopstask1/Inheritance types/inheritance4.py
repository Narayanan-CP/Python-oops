# this is called Hierarchial level inheritance
#the important point is it has only one parent class and two child class
class Grandparent:
    def walk(self):
        print("Grandpa is walking")
        
      
class Parent(Grandparent):
    def __init__(self):
        self.networth=100000
    def swim(self,speed):
        print("parents is swimming",speed) 
        
     
class Child(Grandparent):
    def drive(self,speed):
        print("Child is driving",speed)
         
         
child1=Child()
parent1=Parent()


print(child1.networth)
child1.walk()


         
         
                      