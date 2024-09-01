class Usermanager:
    __Users=[]
    
    @classmethod
    def AddUser(cls,user):
        cls.__Users.append(user)