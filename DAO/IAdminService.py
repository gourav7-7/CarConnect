from abc import ABC,abstractmethod



class IAdminService(ABC): 

    @abstractmethod
    def GetAdminById(self, adminId):
        pass 

    @abstractmethod
    def GetAdminByUsername(self, username):
        pass 

    @abstractmethod
    def RegisterAdmin(self, adminData):
        pass 

    @abstractmethod
    def UpdateAdmin(self, adminData):
        pass 

    @abstractmethod
    def DeleteAdmin(self, adminId):
        pass 