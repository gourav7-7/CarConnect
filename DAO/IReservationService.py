from abc import ABC,abstractmethod


class IReservationService(ABC): 
    
    @abstractmethod
    def GetReservationById(self, reservationId):
        pass 
    
    @abstractmethod
    def GetReservationsByCustomerId(self, customerId):
        pass 
    
    @abstractmethod
    def CreateReservation(self, reservationData):
        pass 
    
    @abstractmethod
    def UpdateReservation(self, reservationData):
        pass 
    
    @abstractmethod
    def CancelReservation(self, reservationId):
        pass