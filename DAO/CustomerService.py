from DAO.ICustomerService import ICustomerService
from Entity.Customer import Customer
from util.DBPropertyUtil import DBProprtyUtil
from util.DBconnutil import DBconnutil


conn_str = DBProprtyUtil.getConnectionString('CarConnect')
conn = DBconnutil.getConnection(conn_str)
stmt=conn.cursor() 



class CustomerService(ICustomerService) :
    def GetCustomerById(self,customerId):
        self.customerID = customerId
        stmt.execute(f'select * from customer where CustomerID = {self.customerID}')
        row = stmt.fetchall() 
        print(row)
        stmt.close()  
        conn.close()


    def GetCustomerByUsername(self,username):
        self.username = username
        stmt.execute(f'select * from customer where FirstName = "{self.username}"')
        # print(type(self.username))
        row = stmt.fetchall()
        print(row)
        stmt.close()  
        conn.close()


    def RegisterCustomer(self, custData):
        self.custData = custData
        stmt.execute(f"INSERT INTO customer VALUES ('{self.custData.getFirstName()}', '{self.custData.getLastName()}', '{self.custData.getEmail()}', '{self.custData.getPhoneNumber()}', '{self.custData.getAddress()}', '{self.custData.getUsername()}', '{self.custData.getPassword()}', '{self.custData.getRegistrationDate()}')")
        conn.commit()
        print("Customer registered successfully!")
        stmt.close()
        conn.close()



    def UpdateCustomer(self,customerData):
        self.customerData = customerData
        stmt.execute(f"UPDATE customer SET FirstName='{self.customerData.getFirstName()}', LastName='{self.customerData.getLastName()}', Email='{self.customerData.getEmail()}', PhoneNumber='{self.customerData.getPhoneNumber()}', Address='{self.customerData.getAddress()}', Username='{self.customerData.getUsername()}', Password='{self.customerData.getPassword()}' WHERE CustomerID={self.customerData.getCustomerID()}")

        conn.commit()
        print("Customer information updated successfully!")
        stmt.close()  
        conn.close()


    def DeleteCustomer(self,customerId):
        self.customerID = customerId
        stmt.execute("DELETE FROM customer WHERE CustomerID=%s", (self.customerID,))
        conn.commit()
        print("Customer deleted successfully!") 
        stmt.close()  
        conn.close()






