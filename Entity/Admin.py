

class Admin:
    def __init__(self):
        self.__AdminID = '' 
        self.__FirstName = '' 
        self.__LastName = '' 
        self.__Email = '' 
        self.__PhoneNumber = '' 
        self.__Username = '' 
        self.__Password = ''
        self.__Role = ''
        self.__JoinDate = ''


    # Setter

    def setAdminID(self,AdminID):
        self.__AdminID = AdminID

    def setFirstName(self,FirstName):
        self.__FirstName = FirstName
    
    def setLastName(self,LastName):
        self.__LastName = LastName

    def setEmail(self,Email):
        self.__Email = Email

    def setPhoneNumber(self,PhoneNumber):
        self.__PhoneNumber = PhoneNumber

    def setUsername(self,Username):
        self.__Username = Username

    def setPassword(self,Password):
        self.__Password = Password

    def setRole(self,Role):
        self.__Role = Role

    def setJoinDate(self,JoinDate):
        self.__JoinDate = JoinDate


        # Getter

    def getAdminID(self):
        return self.__AdminID

    def getFirstName(self):
        return self.__FirstName
    
    def getLastName(self):
        return self.__LastName

    def getEmail(self):
        return self.__Email 

    def getPhoneNumber(self):
        return self.__PhoneNumber

    def getUsername(self):
        return self.__Username 

    def getPassword(self):
        return self.__Password 

    def getRole(self):
        return self.__Role 

    def getJoinDate(self):
        return self.__JoinDate