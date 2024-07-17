#here we have used mro which is called as method resolution order.
class Parent:
    def Sing(self):
        print("Parent is singing")
class Relative:
    def Sing(self):
        print("Relative is singing")
        
class Child(Relative,Parent):
    def Common(self):
        super(Relative,self).Sing()
        
        
        
child1=Child()
child1.Common()
#if we want to use it by class name means we want to pass the object name as an argument.    
Parent.Sing(child1)                    