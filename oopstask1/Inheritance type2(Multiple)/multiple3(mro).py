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