
class Vehicle:
    def __init__(self):
        self.__VehicleID = '',
        self.__Model = '', 
        self.__Make = '', 
        self.__Year = '',
        self.__Color = '',
        self.__RegistrationNumber = '',
        self.__Availability = '', 
        self.__DailyRate = '' 

# Setters
    def  setVehicleID(self,VehicleID):
        self.__VehicleID = VehicleID

    def  setModel(self,Model):
        self.__Model = Model    
        
    def  setMake(self,Make):
        self.__Make = Make

    def  setYear(self,Year):
        self.__Year = Year

    def  setColor(self,Color):
        self.__Color = Color

    def  setRegistrationNumber(self,RegistrationNumber):
        self.__RegistrationNumber = RegistrationNumber

    def  setAvailability(self,Availability):
        self.__Availabilityrname = Availability

    def  setDailyRate(self,DailyRate):
        self.__DailyRate = DailyRate


# getters
    def  getVehicleID(self):
        return self.__VehicleID

    def  getModel(self):
        return self.__Model    
        
    def  getMake(self):
        return self.__Make 

    def  getYear(self):
        return self.__Year 

    def  getColor(self):
        return self.__Color 

    def  getRegistrationNumber(self):
        return self.__RegistrationNumber 

    def  getAvailability(self):
        return self.__Availabilityrname 

    def  getDailyRate(self):
        return self.__DailyRate



