from abc import ABC, abstractmethod  

class IVehicleService(ABC):
    
    @abstractmethod
    def GetVehicleById(self, vehicleId):
        pass

    @abstractmethod
    def GetAvailableVehicles(self ):
        pass 

    @abstractmethod
    def AddVehicle(self, vehicleData):
        pass 

    @abstractmethod
    def UpdateVehicle(self, vehicleData):
        pass 

    @abstractmethod
    def RemoveVehicle(self, vehicleId):
        pass 