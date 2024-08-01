# 1st rule:if we write two functions with same name in python it takes the function which used 
# lastly where as in other programming languages we can access it using the argument for example if we give one parameter it takes first sleep,if we give 
# two parameters it will call second sleep method
class Person:
    def __init__(self,name,age):
        self.Name=name
        self.Age=age
    def Sleep(self,sleepinghours):
        print("Sleeping hours is:",sleepinghours)
    def Sleep(self,start,end):
        print("Sleeping hours is:",end-start)  
        
person1=Person("Narayanan",20)
person1.Sleep(8,6)              
person1.Sleep(8)              