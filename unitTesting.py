import unittest
from DAO.AuthenticationService import AuthenticationService
from DAO.CustomerService import CustomerService
from DAO.VehicleService import VehicleService
from Entity.Customer import Customer
from Entity.Vehicle import Vehicle

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.authServ = AuthenticationService("CarConnect") 
        self.custServ = CustomerService()
        self.vehiServ = VehicleService()

    # def testAuthUserTrue(self):
    #     # Assuming there exists a user with valid credentials in the test database
    #     username = input("Enter Valid Username : ")
    #     password = input("Enter Valid Password : ")
    #     result = self.authServ.authenticate_user(username, password)
    #     self.assertEqual(result, "User Authenticated")

    def testAuthUserFalse(self):
        # Assuming there is no user with these credentials in the test database
        username = input("Enter Invalid Username : ")
        password = input("Enter Invalid Password : ")
        result = self.authServ.authenticate_user(username, password)
        self.assertEqual(result, "Try Again")

    def testRegCust(self):
        
        testCust = Customer()
        testCust.setCustomerID(int(input("Enter CustomerID : ")))
        testCust.setFirstName(input("Enter First Name : "))
        testCust.setLastName(input("Enter Last Name"))
        testCust.setEmail(input("Enter Email : "))
        testCust.setPhoneNumber(input("Enter Phone Number : "))
        testCust.setAddress(input("Enter Address : "))
        testCust.setUsername(input("Enter Username : "))
        testCust.setPassword(input("Enter Password"))
        testCust.setRegistrationDate(input("Enter Date (YYYY-MM-DD) : "))

        self.custServ.RegisterCustomer(testCust)

        regCust = self.custServ.GetCustomerById(testCust.getCustomerID())

        
        self.assertEqual(regCust[0][0], testCust.getCustomerID())

    def testAddVehi(self):
        
        testVehi = Vehicle()
        testVehi.setVehicleID(int(input("Enter Vehicle ID : ")))
        testVehi.setMake(input("Enter Make of Vehicle : "))
        testVehi.setModel(input("Enter Model of Vehicle : "))
        testVehi.setYear(input("Enter Year : "))
        testVehi.setColor(input("Enter Color : "))
        testVehi.setRegistrationNumber(input("Enter Registration Number : "))
        testVehi.setAvailability(int(input("Enter 1 for Available or 0 for Unavailable: ")))
        testVehi.setDailyRate(float(input("Enter Daily Rate : ")))

        
        self.vehiServ.AddVehicle(testVehi)

        
        addedVehi = self.vehiServ.GetVehicleById(testVehi.getVehicleID())

        
        self.assertEqual(addedVehi[0][0], testVehi.getVehicleID()) 

    def testGetAvailableVehi(self):
       
        res = self.vehiServ.GetAvailableVehicles()
        self.assertEqual("True",str(res))

    def testGetAllVehi(self):
        
        res = self.vehiServ.GetAllVehicles()
        self.assertEqual("True",str(res))

if __name__ == '__main__':
    unittest.main()
