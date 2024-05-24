import datetime
class Reservation:
    def __init__(self):
        self.__ReservationID = '' 
        self.__CustomerID = '' 
        self.__VehicleID = ''
        self.__StartDate = ''
        self.__EndDate = ''
        self.__TotalCost = ''
        self.__Status = ''

# Setters

    def setReservationID(self,ReservationID):
       self.__ReservationID = ReservationID

    def setCustomerID(self,CustomerID):
       self.__CustomerID = CustomerID

    def setVehicleID(self,VehicleID):
       self.__VehicleID = VehicleID

    def setStartDate(self,StartDate):
       self.__StartDate = datetime.datetime.strptime(StartDate, '%Y-%m-%d').date()

    def setEndDate(self,EndDate):
       self.__EndDate = datetime.datetime.strptime(EndDate, '%Y-%m-%d').date()

    def setTotalCost(self,TotalCost):
       self.__TotalCost = TotalCost

    def setStatus(self,Status):
       self.__Status = Status
    
# Getters

    def getReservationID(self):
       return self.__ReservationID

    def getCustomerID(self):
       return self.__CustomerID 

    def getVehicleID(self):
       return self.__VehicleID

    def getStartDate(self):
       return self.__StartDate

    def getEndDate(self):
       return self.__EndDate

    def getTotalCost(self):
       return self.__TotalCost
    
    def CalculateTotalCost(self):
       pass
    
    def getStatus(self):
       return self.__Status