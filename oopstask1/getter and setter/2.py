class Person:
    def __init__(self):
        #If it is a public variable means we can ADD the name at outside by specifying it,so when we use getter and setter we make variables as private
        # so only we use private method which is accesible only inside the class.
        self.__name=None
        #setter
    def SetName(self,value):
        if(len(value)>20):
            print("please enter lesser value")
        else:
            self.__name=value
        #getter     
    def GetName(self):
        if self.__name==None:
            print("Please Enter valueable name")
            
        return self.__name       
        
person1=Person()
person1.SetName("Akil")  
print(person1.GetName())     
         