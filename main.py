from DAO.CustomerService import CustomerService
from DAO.AdminService import AdminService
from DAO.VehicleService import VehicleService
from DAO.ReservationService import ReservationService
from DAO.AuthenticationService import AuthenticationService
from Entity.Customer import Customer
from Entity.Vehicle import Vehicle
from Entity.Reservation import Reservation
from Entity.Admin import Admin
from Exceptions.AuthenticationException import *
from Exceptions.DatabaseConnectionException import *
from Exceptions.AdminNotFoundException import *
from Exceptions.InvalidInputException import *
from Exceptions.ReservationException import *
from Exceptions.VehicleNotFoundException import *

class MainMenu:
    def __init__(self):
        self.authServ = AuthenticationService("CarConnect")
        self.custServ = CustomerService()
        self.vehiServ = VehicleService()
        self.resvServ = ReservationService()
        self.adminServ = AdminService()


    def Menu(self):
        print("\ Main Menu : ")
        print("1. Authenticate User")
        print("2. Get Customer by ID")
        print("3. Get Customer by Username")
        print("4. Register New Customer")
        print("5. Update Existing Customer")
        print("6. Delete Customer")
        print("7. Get Vehicle by ID")
        print("8. Get Available Vehicles")
        print("9. Add Vehicle")
        print("10. Update Existing Vehicle")
        print("11. Remove Vehicle")
        print("12. Get Reservation by ID")
        print("13. Get Reservation by Customer ID")
        print("14. Create Reservation")
        print("15. Update Reservation")
        print("16. Cancel Reservation")
        print("17. Get Admin by ID")
        print("18. Get Admin by Username")
        print("19. Register Admin")
        print("20. Update Admin")
        print("21. Delete Admin")
        print("22. Exit")

    
    def authUser(self):
        uname = input("Enter Usernamr : ")
        passwd = input("Enter Password : ")

        try:
            authentication = self.authServ.authenticate_user(uname,passwd)
            if authentication:
                print("Authentication Successfull!")
            else:
                print("TRY AGAIN")
        except AuthenticationException as e:
            print(e)

    def getCustomerByID(self):
        custID = int(input("Enter Customer ID : "))
        try:
            self.custServ.GetCustomerById(custID)
        except InvalidInputException as e:
            print(e)

    def getCustomerByUname(self):
        uname = input("Enter Customer Username : ")
        try:
            self.custServ.GetCustomerByUsername(uname)
        except InvalidInputException as e:
            print(e)

    def regCustomer(self):
        cust = Customer()
        cust.setCustomerID(int(input("Enter Customer ID : ")))
        cust.setFirstName(input("Enter First Nmae : "))
        cust.setLastName(input("Enter Last Name : "))
        cust.setEmail(input("Enter Customer Email : "))
        cust.setPhoneNumber(input("Enter Phone number : "))
        cust.setAddress(input("Enter Address : "))
        cust.setUsername(input("Enter Username : "))
        cust.setPassword(input("Enter Password : "))
        cust.setRegistrationDate(input("Enter Registration Date (YYYY-MM-DD) : "))
        try:
            self.custServ.RegisterCustomer(cust)
        except InvalidInputException as e:
            print(e)        

    def updateCustomer(self):
        cust = Customer()
        cust.setCustomerID(int(input("Enter Customer ID to Update : ")))
        cust.setFirstName(input("Enter First Nmae : "))
        cust.setLastName(input("Enter Last Name : "))
        cust.setEmail(input("Enter Customer Email : "))
        cust.setPhoneNumber(input("Enter Phone number : "))
        cust.setAddress(input("Enter Address : "))
        cust.setUsername(input("Enter Username : "))
        cust.setPassword(input("Enter Password : "))
        cust.setRegistrationDate(input("Enter Registration Date (YYYY-MM-DD) : "))
        try:
            self.custServ.UpdateCustomer(cust)
        except InvalidInputException as e:
            print(e)

    def deleteCust(self):
        custID = int(input("Enter Customer ID to Delete : "))
        try:
            self.custServ.DeleteCustomer(custID)
        except InvalidInputException as e:
            print(e)

    def getVehiByID(self):
        v_ID = int(input("Enter Vehicle ID : "))
        try:
            self.vehiServ.GetVehicleById(v_ID)
        except VehicleNotFoundException as e:
            print(e)

    def getAvailableVehi(self):
        try:
            self.vehiServ.GetAvailableVehicles()
        except VehicleNotFoundException as e:
            print(e)

    def addVehi(self):
        vehi = Vehicle()
        vehi.setVehicleID(int(input("Enter Vehicle ID : ")))
        vehi.setMake(input("Enter Make of Vehicle : "))
        vehi.setModel(input("Enter Model of Vehicle : "))
        vehi.setYear(input("Enter Year : "))
        vehi.setColor(input("Enter Color : "))
        vehi.setRegistrationNumber(input("Enter Registration Number : "))
        vehi.setAvailability(int(input("Enter 1 for Available or 0 for Unavailable: ")))
        vehi.setDailyRate(float(input("Enter Daily Rate : ")))
        try:
            self.vehiServ.AddVehicle(vehi)
        except InvalidInputException as e:
            print(e)

    def updateVehi(self):
        vehi = Vehicle()
        vehi.setVehicleID(int(input("Enter Vehicle ID to update : ")))
        vehi.setMake(input("Enter Make of Vehicle : "))
        vehi.setModel(input("Enter Model of Vehicle : "))
        vehi.setYear(input("Enter Year : "))
        vehi.setColor(input("Enter Color : "))
        vehi.setRegistrationNumber(input("Enter Registration Number : "))
        vehi.setAvailability(int(input("Enter 1 for Available or 0 for Unavailable: ")))
        vehi.setDailyRate(float(input("Enter Daily Rate : ")))
        try:
            self.vehiServ.UpdateVehicle(vehi)
        except VehicleNotFoundException as e:
            print(e)

    def rmVehi(self):
        try:
            self.vehiServ.RemoveVehicle(int(input("Enter vehicle ID to remove : ")))
        except VehicleNotFoundException as e:
            print(e)

    def getResByID(self):
        resID = int(input("Enter Reservation ID : "))
        try:
            self.resvServ.GetReservationById(resID)
        except ReservationException as e:
            print(e)

    def getResByCustID(self):
        custID = int(input("Enter Customer ID : "))
        try:
            self.resvServ.GetReservationsByCustomerId(custID)
        except ReservationException as e:
            print(e)

    def createRes(self):
        resv = Reservation()
        resv.setReservationID(int(input("Enter Reservation ID : ")))
        resv.setCustomerID(int(input("Enter Customer ID : ")))
        resv.setVehicleID(int(input("Enter Vehicle ID : ")))
        resv.setStatus(input("Enter Status ( pending, confirmed, completed) : "))
        resv.setStartDate(input("Enter Start Date (YYYY-MM-DD) : "))
        resv.setEndDate(input("Enter End Date (YYYY-MM-DD) : "))  
        resv.setTotalCost(float(input("Enter total cost : ")))
        try:
            self.resvServ.CreateReservation(resv)
        except ReservationException as e:
            print(e)

    def updateRes(self):
        resv = Reservation()
        resv.setReservationID(int(input("Enter Reservation ID To UPDATE : ")))
        resv.setCustomerID(int(input("Enter Customer ID : ")))
        resv.setVehicleID(int(input("Enter Vehicle ID : ")))
        resv.setStatus(input("Enter Status ( pending, confirmed, completed) : "))
        resv.setStartDate(input("Enter Start Date (YYYY-MM-DD) : "))
        resv.setEndDate(input("Enter End Date (YYYY-MM-DD) : "))  
        resv.setTotalCost(float(input("Enter total cost : ")))
        try:
            self.resvServ.UpdateReservation(resv)
        except ReservationException as e:
            print(e)

    def cancelRes(self):
        resID = int(input("Enter Reservation ID to cancel : "))
        try:
            self.resvServ.CancelReservation(resID)
        except InvalidInputException as e:
            print(e)

    def getAdminByID(self):
        adminid = int(input("Enter Admin ID : "))
        try:
            self.adminServ.GetAdminById(adminid)
        except AdminNotFoundException as e:
            print(e)

    def getAdminByUname(self):
        auname = input("Enter Admin Username : ")
        try:
            self.adminServ.GetAdminByUsername(auname)
        except AdminNotFoundException as e:
            print(e)

    def regAdmin(self):
        ad = Admin()
        ad.setAdminID(int(input("Enter Admin ID : ")))
        ad.setFirstName(input("Enter First Name : "))
        ad.setLastName(input("Enter Last Name : "))
        ad.setPhoneNumber(input("Enter Phone Number : "))
        ad.setEmail(input("Enter Email : "))
        ad.setRole(input("Enter Role : "))
        ad.setUsername(input("Enter UserName : "))
        ad.setPassword(input("Enter PassWord : "))
        ad.setJoinDate(input("Enter Joining Date (YYYY-MM-DD) : "))
        try:
            self.adminServ.RegisterAdmin(ad)
        except InvalidInputException as e:
            print(e)

    def updateAdmin(self):
        ad = Admin()
        ad.setAdminID(int(input("Enter Admin ID To UPDATE : ")))
        ad.setFirstName(input("Enter First Name : "))
        ad.setLastName(input("Enter Last Name : "))
        ad.setPhoneNumber(input("Enter Phone Number : "))
        ad.setEmail(input("Enter Email : "))
        ad.setRole(input("Enter Role : "))
        ad.setUsername(input("Enter UserName : "))
        ad.setPassword(input("Enter PassWord : "))
        ad.setJoinDate(input("Enter Joining Date (YYYY-MM-DD) : "))
        try: 
            self.adminServ.UpdateAdmin(ad)
        except AdminNotFoundException as e:
            print(e)
    
    def deleteAdmin(self):
        adminid = int(input("Enter Admin ID to Delete : "))
        try:
            self.adminServ.DeleteAdmin(adminid)
        except AdminNotFoundException as e:
            print(e)

    def Exit(self):
        print("Exiting ...")

    def run(self):
        while True:
            self.Menu()
            choice = input("Enter your choice : ")
            if choice == "1":
                self.authUser()
            elif choice == "2":
                self.getCustomerByID()
            elif choice == "3":
                self.getCustomerByUname()
            elif choice == "4":
                self.regCustomer()
            elif choice == "5":
                self.updateCustomer()
            elif choice == "6":
                self.deleteCust()
            elif choice == "7":
                self.getVehiByID()
            elif choice == "8":
                self.getVehiByID()
            elif choice == "9":
                self.addVehi()
            elif choice == "10":
                self.updateVehi()
            elif choice == "11":
                self.rmVehi()
            elif choice == "12":
                self.getResByID()
            elif choice == "13":
                self.getResByCustID()
            elif choice == "14":
                self.createRes()
            elif choice == "15":
                self.updateRes()
            elif choice == "16":
                self.cancelRes()
            elif choice == "17":
                self.getAdminByID()
            elif choice == "18":
                self.getAdminByUname()
            elif choice == "19":
                self.regAdmin()
            elif choice == "20":
                self.updateAdmin()
            elif choice == "21":
                self.deleteAdmin()
            elif choice == "22":
                self.Exit()
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 22.")

if __name__ == "__main__":
    menu = MainMenu()
    menu.run()




