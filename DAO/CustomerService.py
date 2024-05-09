from DAO.ICustomerService import ICustomerService
from Entity.Customer import Customer
from util.DBPropertyUtil import DBProprtyUtil
from util.DBconnutil import DBconnutil
from Exceptions.InvalidInputException import InvalidInputException



class CustomerService(ICustomerService) :
    def GetCustomerById(self,customerId):
        conn = DBconnutil.getConnection(DBProprtyUtil.getConnectionString('CarConnect'))
        stmt = conn.cursor()
        self.customerID = customerId
        stmt.execute(f'select * from customer where CustomerID = {self.customerID}')
        row = stmt.fetchall() 
        stmt.close()  
        conn.close()
        return row


    def GetCustomerByUsername(self,username):
        conn = DBconnutil.getConnection(DBProprtyUtil.getConnectionString('CarConnect'))
        stmt = conn.cursor()
        self.username = username
        stmt.execute(f'select * from customer where FirstName = "{self.username}"')
        # print(type(self.username))
        row = stmt.fetchall()
        stmt.close()  
        conn.close()
        return row


    def RegisterCustomer(self, custData):
        conn = DBconnutil.getConnection(DBProprtyUtil.getConnectionString('CarConnect'))
        stmt = conn.cursor()
        self.custData = custData
        stmt.execute(f"INSERT INTO customer VALUES ({self.custData.getCustomerID()},'{self.custData.getFirstName()}', '{self.custData.getLastName()}', '{self.custData.getEmail()}', '{self.custData.getPhoneNumber()}', '{self.custData.getAddress()}', '{self.custData.getUsername()}', '{self.custData.getPassword()}', '{self.custData.getRegistrationDate()}')")
        conn.commit()
        print("Customer registered successfully!")
        stmt.close()
        conn.close()



    def UpdateCustomer(self, customerData):
        conn = DBconnutil.getConnection(DBProprtyUtil.getConnectionString('CarConnect'))
        stmt = conn.cursor()
        self.customerData = customerData
        
        stmt.execute(f"SELECT * FROM customer WHERE CustomerID = {self.customerData.getCustomerID()}")
        exists = stmt.fetchone()
        
        if exists:
            
            stmt.execute(f"UPDATE customer SET FirstName='{self.customerData.getFirstName()}', LastName='{self.customerData.getLastName()}', Email='{self.customerData.getEmail()}', PhoneNumber='{self.customerData.getPhoneNumber()}', Address='{self.customerData.getAddress()}', Username='{self.customerData.getUsername()}', Password='{self.customerData.getPassword()}' WHERE CustomerID={self.customerData.getCustomerID()}")
            conn.commit()
            print("Customer information updated successfully!")
        else:
           
            raise InvalidInputException()

        stmt.close()  
        conn.close()


    def DeleteCustomer(self,customerId):
        conn = DBconnutil.getConnection(DBProprtyUtil.getConnectionString('CarConnect'))
        stmt = conn.cursor()
        self.customerID = customerId
        stmt.execute(f"selecct * from customer where CustomerID = {self.customerID}")
        existing = stmt.fetchone
        if existing is None:
            stmt.close()
            conn.close()
            raise InvalidInputException()
        
        stmt.execute(f"DELETE FROM customer WHERE CustomerID={self.customerID}")
        conn.commit()
        print("Customer deleted successfully!") 
        stmt.close()  
        conn.close()






