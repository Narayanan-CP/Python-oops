class Person:
    def __init__(self):
        #In private variable we can ADD the name
        # only by using public method and it is accesible only inside the class.
        self.__name=None
    def SetName(self,value):
        if(len(value)>20):
            print("please enter lesser value")
        else:
            self.__name=value 
    def GetName(self):
        if self.__name==None:
            print("Please Enter valueable name")
            
        return self.__name       
        
person1=Person()
person1.SetName("Akil")  
print(person1.GetName())     
         