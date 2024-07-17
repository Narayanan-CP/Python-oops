# _ => means protected.
class School:
    def __init__(self):
        self.name="narayanan"
        self.age=21
        self._salary=1000000000
class Faculty(School):
    def Revenue(self):
        print(self._salary/2)           
child1=Faculty()
print(child1._salary )  
child1.Revenue()     