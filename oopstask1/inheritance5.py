# this is called Hybrid level inheritance
class Grandparent:
    def walk(self):
        print("Grandpa is walking")
        
class Relative(Grandparent):
    def chat(self):
        print("Relatives are chatting")  
         
class Parent(Grandparent):
    def __init__(self):
        self.networth=100000
    def swim(self,speed):
        print("parents is swimming",speed) 
        
    
class Child(Parent,Relative):
    def drive(self,speed):
        print("Child is driving",speed)
         
         
child1=Child()
parent1=Parent()

print(child1.networth)
child1.walk()


         
         
                      