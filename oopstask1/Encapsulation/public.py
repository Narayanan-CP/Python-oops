# it is just like a normal program just understand th control flow.
class School:
    def __init__(self):
        self.name="narayanan"
        self.age=21
        self.__salary=30000000
        
    def __private(self):
        print(self.__salary//2)    
    def common(self):
        self.__private()    
child1=School()
child1.common()        