# compile time polymorphism
class Person:
    def __init__(self,name,age):
        self.Name=name
        self.Age=age
    def Sleep(self,sleepinghours=0,start=None,end=None):
        if start!=None and end !=None:
            print("Sleeping hours is:",end-start)
        else:
            print("sleeping hours is:",sleepinghours)    
 
person1=Person("narayanan",20)
person1.Sleep(start=20,end=24)#this is how we can use methodoverloadibg in python.
        