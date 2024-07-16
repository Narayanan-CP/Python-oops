class Parent:
    def __init__(self,Networth):
        self.Networth=Networth
class Child(Parent):
    def __init__(self,Networth):
        #the below super __init__ refers to the Parent class Networth
        super().__init__(Networth)
        print("Child class is invoked")
    
    
    def Childnetworth(self):
        #the above networth is invoked from the parent class
        print(self.Networth//2)     
               
child1=Child(100000)
print(child1.Networth) 
child1.Childnetworth()                   