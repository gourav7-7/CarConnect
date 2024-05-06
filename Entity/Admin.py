

class Admin:
    def __init__(self):
        self.AdminID = '' 
        self.FirstName = '' 
        self.LastName = '' 
        self.Email = '' 
        self.PhoneNumber = '' 
        self.Username = '' 
        self.Password = ''
        self.Role = ''
        self.JoinDate = ''


    # Setter

    def setAdminID(self,AdminID):
        self.AdminID = AdminID

    def setFirstName(self,FirstName):
        self.FirstName = FirstName
    
    def setLastName(self,LastName):
        self.LastName = LastName

    def setEmail(self,Email):
        self.Email = Email

    def setPhoneNumber(self,PhoneNumber):
        self.PhoneNumber = PhoneNumber

    def setUsername(self,Username):
        self.Username = Username

    def setPassword(self,Password):
        self.Password = Password

    def setRole(self,Role):
        self.Role = Role

    def setJoinDate(self,JoinDate):
        self.JoinDate = JoinDate


        # Getter

    def getAdminID(self):
        return self.AdminID

    def getFirstName(self):
        return self.FirstName
    
    def getLastName(self):
        return self.LastName

    def getEmail(self):
        return self.Email 

    def getPhoneNumber(self):
        return self.PhoneNumber

    def getUsername(self):
        return self.Username 

    def getPassword(self):
        return self.Password 

    def getRole(self):
        return self.Role 

    def getJoinDate(self):
        return self.JoinDate