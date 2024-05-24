import datetime

class Customer:
    def __init__(self):
        self.__CustomerID = '', 
        self.__FirstName = '',
        self.__LastName = '',
        self.__Email = '',
        self.__PhoneNumber = '',
        self.__Address = '', 
        self.__Username = '', 
        self.__Password = '', 
        self.__RegistrationDate = ''


    
    # Setters
    def  setCustomerID(self,CustomerID):
        self.__CustomerID = CustomerID

    def  setFirstName(self,FirstName):
        self.__FirstName = FirstName    
        
    def  setLastName(self,LastName):
        self.__LastName = LastName

    def  setEmail(self,Email):
        self.__Email = Email

    def  setPhoneNumber(self,PhoneNumber):
        self.__PhoneNumber = PhoneNumber

    def  setAddress(self,Address):
        self.__Address = Address

    def  setUsername(self,Username):
        self.__Username = Username

    def  setPassword(self,Password):
        self.__Password = Password

    def  setRegistrationDate(self,RegistrationDate):
        self.__RegistrationDate = datetime.datetime.strptime(RegistrationDate, '%Y-%m-%d').date()


    # Getters

    def getCustomerID(self):
        return self.__CustomerID
    
    def  getFirstName(self):
        return self.__FirstName
        
    def  getLastName(self):
        return self.__LastName

    def  getEmail(self):
        return self.__Email

    def  getPhoneNumber(self):
        return self.__PhoneNumber 

    def  getAddress(self):
        return self.__Address 

    def  getUsername(self):
        return self.__Username

    def  getPassword(self):
        return self.__Password

    def  getRegistrationDate(self):
        return self.__RegistrationDate
    
    
    def Athenticate(self,Password):
        if self.__Password == Password:
            print('Login Successful ')
        else:
            print('TRY AGAIN !!!')

