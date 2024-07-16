class Grandparent:
    def drive(self):
        print("Grandpa is driving")
class Parent(Grandparent):
    def drive(self): 
        # the below super refers to the Parent class and if we call  the parent class it will call the grandparent class
        super().drive()
        
        print("Parent is driving")       
child1=Parent()  
child1.drive()     