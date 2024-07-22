class Person:
    def __init__(self):
        #In private variable we can ADD the name
        # only by using public method and it is accesible only inside the class.
        self.__name=None
    def SetName(self,value):
        self.__name=value 
    def GetName(self):
        return self.__name       
        
person1=Person()
person1.SetName("Akil")  
print(person1.GetName())     
         