class Person:
    def __init__(self):        
        self.__name=None
        self.__age=None
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,value):
        if value<0:
            print("Enter proper age")
        else:
            self.__age=value    
            
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
person1.age=-1
print(person1.age)