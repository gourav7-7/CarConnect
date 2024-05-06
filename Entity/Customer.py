import datetime

class Customer:
    def __init__(self):
        self.CustomerID = '', 
        self.FirstName = '',
        self.LastName = '',
        self.Email = '',
        self.PhoneNumber = '',
        self.Address = '', 
        self.Username = '', 
        self.Password = '', 
        self.RegistrationDate = ''


    
    # Setters
    def  setCustomerID(self,CustomerID):
        self.CustomerID = CustomerID

    def  setFirstName(self,FirstName):
        self.FirstName = FirstName    
        
    def  setLastName(self,LastName):
        self.LastName = LastName

    def  setEmail(self,Email):
        self.Email = Email

    def  setPhoneNumber(self,PhoneNumber):
        self.PhoneNumber = PhoneNumber

    def  setAddress(self,Address):
        self.Address = Address

    def  setUsername(self,Username):
        self.Username = Username

    def  setPassword(self,Password):
        self.Password = Password

    def  setRegistrationDate(self,RegistrationDate):
        self.RegistrationDate = datetime.datetime.strptime(RegistrationDate, '%Y-%m-%d').date()


    # Getters

    def getCustomerID(self):
        return self.CustomerID
    
    def  getFirstName(self):
        return self.FirstName
        
    def  getLastName(self):
        return self.LastName

    def  getEmail(self):
        return self.Email

    def  getPhoneNumber(self):
        return self.PhoneNumber 

    def  getAddress(self):
        return self.Address 

    def  getUsername(self):
        return self.Username

    def  getPassword(self):
        return self.Password

    def  getRegistrationDate(self):
        return self.RegistrationDate
    
    
    def Athenticate(self,Password):
        if self.Password == Password:
            print('Login Successful ')
        else:
            print('TRY AGAIN !!!')

