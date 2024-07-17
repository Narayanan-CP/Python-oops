# -- =>it represents private.
class School:
    def __init__(self):
        self.Name="Abc"
        self.Place="Chennai"
        self.__Revenue=500000
    def SchoolRevenue(self):
        print(self.__Revenue)    
school1=School()
school1.SchoolRevenue()       