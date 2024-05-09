# • Reservation: 
# • Properties: ReservationID, CustomerID, VehicleID, StartDate, EndDate, TotalCost, 
# Status 
# • Methods: CalculateTotalCost() 
import datetime
class Reservation:
    def __init__(self):
        self.ReservationID = '' 
        self.CustomerID = '' 
        self.VehicleID = ''
        self.StartDate = ''
        self.EndDate = ''
        self.TotalCost = ''
        self.Status = ''

# Setters

    def setReservationID(self,ReservationID):
       self.ReservationID = ReservationID

    def setCustomerID(self,CustomerID):
       self.CustomerID = CustomerID

    def setVehicleID(self,VehicleID):
       self.VehicleID = VehicleID

    def setStartDate(self,StartDate):
       self.StartDate = datetime.datetime.strptime(StartDate, '%Y-%m-%d').date()

    def setEndDate(self,EndDate):
       self.EndDate = datetime.datetime.strptime(EndDate, '%Y-%m-%d').date()

    def setTotalCost(self,TotalCost):
       self.TotalCost = TotalCost

    def setStatus(self,Status):
       self.Status = Status
    
# Getters

    def getReservationID(self):
       return self.ReservationID

    def getCustomerID(self):
       return self.CustomerID 

    def getVehicleID(self):
       return self.VehicleID

    def getStartDate(self):
       return self.StartDate

    def getEndDate(self):
       return self.EndDate

    def getTotalCost(self):
       return self.TotalCost
    
    def CalculateTotalCost(self):
       pass
    
    def getStatus(self):
       return self.Status