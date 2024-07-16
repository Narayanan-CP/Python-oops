# this is called multilevel inheritance
class Grandparent:
    def walk(self):
        print("Grandpa is walking")
        
      
class Parent(Grandparent):
    def __init__(self):
        self.networth=100000
    def swim(self,speed):
        print("parents is swimming",speed) 
        
       
class Child(Parent):
    def drive(self,speed):
        print("Child is driving",speed)
         
         
child1=Child()
parent1=Parent()


print(child1.networth)
child1.walk()


         
         
                      