from abc import ABC, abstractmethod

class ICustomerService(ABC): 
    @abstractmethod
    def GetCustomerById(self,customerId):
    
        pass 

    @abstractmethod
    def GetCustomerByUsername(self,username):
   
        pass 


    @abstractmethod    
    def RegisterCustomer(self,customerData):
        
        pass 


    @abstractmethod    
    def UpdateCustomer(self,customerData):
        
        pass 


    @abstractmethod
    def DeleteCustomer(self,customerId):
     
        pass 