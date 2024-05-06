
class Vehicle:
    def __init__(self):
        self.VehicleID = '',
        self.Model = '', 
        self.Make = '', 
        self.Year = '',
        self.Color = '',
        self.RegistrationNumber = '',
        self.Availability = '', 
        self.DailyRate = '' 

# Setters
    def  setVehicleID(self,VehicleID):
        self.VehicleID = VehicleID

    def  setModel(self,Model):
        self.Model = Model    
        
    def  setMake(self,Make):
        self.Make = Make

    def  setYear(self,Year):
        self.Year = Year

    def  setColor(self,Color):
        self.Color = Color

    def  setRegistrationNumber(self,RegistrationNumber):
        self.RegistrationNumber = RegistrationNumber

    def  setAvailability(self,Availability):
        self.Availabilityrname = Availability

    def  setDailyRate(self,DailyRate):
        self.DailyRate = DailyRate


# getters
    def  getVehicleID(self):
        return self.VehicleID

    def  getModel(self):
        return self.Model    
        
    def  getMake(self):
        return self.Make 

    def  getYear(self):
        return self.Year 

    def  getColor(self):
        return self.Color 

    def  getRegistrationNumber(self):
        return self.RegistrationNumber 

    def  getAvailability(self):
        return self.Availabilityrname 

    def  getDailyRate(self):
        return self.DailyRate



