class Person:
    def __init__(self):        
        self.__name=None
    #getter -always getter should be at first    
    @property
    def name(self):
        if self.__name==None:
            print("Please Enter valueable name")            
        return self.__name 
    #setter
    @name.setter   
    def name(self,value):
        if(len(value)>20):
            print("please enter lesser value")
        else:
            self.__name=value
            
   
    
person1=Person()
#this is for setter
person1.name="Narayanan" 
# this is for getter
print(person1.name)  