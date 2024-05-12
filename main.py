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


    def CustomerMenu(self):
        print("\nCustomer Menu: ")
        print("1. Authenticate User")
        print("2. Get Customer by ID")
        print("3. Register New Customer")
        print("4. Update Existing Customer")
        print("5. Delete Customer")
        print("6. Exit")

    def VehicleMenu(self):
        print("\nVehicle Menu: ")
        print("1. Get Vehicle by ID")
        print("2. Get Available Vehicles")
        print("3. Add Vehicle")
        print("4. Update Existing Vehicle")
        print("5. Remove Vehicle")
        print("6. Exit")

    def ReservationMenu(self):
        print("\nReservation Menu: ")
        print("1. Get Reservation by ID")
        print("2. Get Reservation by Customer ID")
        print("3. Create Reservation")
        print("4. Update Reservation")
        print("5. Cancel Reservation")
        print("6. Exit")

    def AdminMenu(self):
        print("\nAdmin Menu: ")
        print("1. Get Admin by ID")
        print("2. Get Admin by Username")
        print("3. Register Admin")
        print("4. Update Admin")
        print("5. Delete Admin")
        print("6. Exit")

    def Menu(self):
        print("\nMain Menu:")
        print("1. Customer")
        print("2. Vehicle")
        print("3. Reservation")
        print("4. Admin")
        print("5. Exit")

    
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
           res = self.custServ.GetCustomerById(custID)
           if res == []:
               raise InvalidInputException
           else:
               print(res)
        except InvalidInputException as e:
            print("Customer Not Found !",e)

    def getCustomerByUname(self):
        uname = input("Enter Customer Username : ")
        try:
            res = self.custServ.GetCustomerByUsername(uname)
            if res == []:
               raise InvalidInputException
            else:
                print(res)
        except InvalidInputException as e:
            print("Customer Not Found !",e)

    def regCustomer(self):
        cust = Customer()
        try:
            cust.setCustomerID(int(input("Enter Customer ID : ")))
            cust.setFirstName(input("Enter First Name : "))
            cust.setLastName(input("Enter Last Name : "))
            cust.setEmail(input("Enter Customer Email : "))
            cust.setPhoneNumber(input("Enter Phone number : "))
            cust.setAddress(input("Enter Address : "))
            cust.setUsername(input("Enter Username : "))
            cust.setPassword(input("Enter Password : "))
            cust.setRegistrationDate(input("Enter Registration Date (YYYY-MM-DD) : "))
        except ValueError:
            print("Invalid input data. Please enter valid input.")
            return  # Return to prevent further execution
    
        try:
            self.custServ.RegisterCustomer(cust)
        except InvalidInputException as e:
            print(e)
  

    def updateCustomer(self):
        try:
            cust = Customer()
            cust.setCustomerID(int(input("Enter Customer ID to Update : ")))
            cust.setFirstName(input("Enter First Name : "))
            cust.setLastName(input("Enter Last Name : "))
            cust.setEmail(input("Enter Customer Email : "))
            cust.setPhoneNumber(input("Enter Phone number : "))
            cust.setAddress(input("Enter Address : "))
            cust.setUsername(input("Enter Username : "))
            cust.setPassword(input("Enter Password : "))
            cust.setRegistrationDate(input("Enter Registration Date (YYYY-MM-DD) : "))
        except ValueError:
            print("Invalid input data. Please enter valid input.")
            return  # Return to prevent further execution
        try:
            self.custServ.RegisterCustomer(cust)
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
            res = self.vehiServ.GetVehicleById(v_ID)
            if res == []:
                raise VehicleNotFoundException
            else:
                print(res)
        except VehicleNotFoundException as e:
            print(e)

    def getAvailableVehi(self):
        try:
            self.vehiServ.GetAvailableVehicles()
        except VehicleNotFoundException as e:
            print(e)

    def addVehi(self):
        try:
            vehi = Vehicle()
            vehi.setVehicleID(int(input("Enter Vehicle ID : ")))
            vehi.setMake(input("Enter Make of Vehicle : "))
            vehi.setModel(input("Enter Model of Vehicle : "))
            vehi.setYear(input("Enter Year : "))
            vehi.setColor(input("Enter Color : "))
            vehi.setRegistrationNumber(input("Enter Registration Number : "))
            vehi.setAvailability(int(input("Enter 1 for Available or 0 for Unavailable: ")))
            vehi.setDailyRate(float(input("Enter Daily Rate : ")))
        except ValueError:
            print("Invalid input data. Please enter valid input.")
            return  # Return to prevent further execution
        try:
            self.vehiServ.AddVehicle(vehi)
        except InvalidInputException as e:
            print(e)

    def updateVehi(self):
        try:
            vehi = Vehicle()
            vehi.setVehicleID(int(input("Enter Vehicle ID to update : ")))
            vehi.setMake(input("Enter Make of Vehicle : "))
            vehi.setModel(input("Enter Model of Vehicle : "))
            vehi.setYear(input("Enter Year : "))
            vehi.setColor(input("Enter Color : "))
            vehi.setRegistrationNumber(input("Enter Registration Number : "))
            vehi.setAvailability(int(input("Enter 1 for Available or 0 for Unavailable: ")))
            vehi.setDailyRate(float(input("Enter Daily Rate : ")))
        except ValueError:
            print("Invalid input data. Please enter valid input.")
            return  # Return to prevent further execution
        try:
            self.vehiServ.UpdateVehicle(vehi)
        except VehicleNotFoundException as e:
            print(e)

    def rmVehi(self):
        try:
            self.vehiServ.RemoveVehicle(int(input("Enter vehicle ID to remove : ")))
        except VehicleNotFoundException as e:
            print(e)

    def getAvVehi(self):
        try:
            self.vehiServ.GetAvailableVehicles()
        except VehicleNotFoundException as e:
            print(e)


    def getResByID(self):
        resID = int(input("Enter Reservation ID : "))
        try:
            res = self.resvServ.GetReservationById(resID)
            if res == []:
                raise ReservationException
            else:
                print(res)
        except ReservationException as e:
            print(e)

    def getResByCustID(self):
        custID = int(input("Enter Customer ID : "))
        try:
            res = self.resvServ.GetReservationsByCustomerId(custID)
            if res == []:
                raise ReservationException
            else:
                print(res)
        except ReservationException as e:
            print(e)

    def createRes(self):
        try:
            resv = Reservation()
            resv.setReservationID(int(input("Enter Reservation ID : ")))
            resv.setCustomerID(int(input("Enter Customer ID : ")))
            resv.setVehicleID(int(input("Enter Vehicle ID : ")))
            resv.setStatus(input("Enter Status ( pending, confirmed, completed) : "))
            resv.setStartDate(input("Enter Start Date (YYYY-MM-DD) : "))
            resv.setEndDate(input("Enter End Date (YYYY-MM-DD) : "))  
            resv.setTotalCost(float(input("Enter total cost : ")))
        except ValueError:
            print("Invalid input data. Please enter valid input.")
            return  # Return to prevent further execution
        try:
            self.resvServ.CreateReservation(resv)
            raise ReservationException("Invalid Input Field, Check Values Again")
        except ReservationException as e:
            print(e)

    def updateRes(self):
        try:
            resv = Reservation()
            resv.setReservationID(int(input("Enter Reservation ID To UPDATE : ")))
            resv.setCustomerID(int(input("Enter Customer ID : ")))
            resv.setVehicleID(int(input("Enter Vehicle ID : ")))
            resv.setStatus(input("Enter Status ( pending, confirmed, completed) : "))
            resv.setStartDate(input("Enter Start Date (YYYY-MM-DD) : "))
            resv.setEndDate(input("Enter End Date (YYYY-MM-DD) : "))  
            resv.setTotalCost(float(input("Enter total cost : ")))
        except ValueError:
            print("Invalid input data. Please enter valid input.")
            return  # Return to prevent further execution
        try:
            self.resvServ.UpdateReservation(resv)
        except ReservationException as e:
            print(e)

    def cancelRes(self):
        resID = int(input("Enter Reservation ID to cancel : "))
        try:
            self.resvServ.CancelReservation(resID)
        except ReservationException as e:
            print(e)

    def getAdminByID(self):
        adminid = int(input("Enter Admin ID : "))
        try:
            res = self.adminServ.GetAdminById(adminid)
            if res == []:
                raise AdminNotFoundException
            else:
                print(res)
        except AdminNotFoundException as e:
            print(e)

    def getAdminByUname(self):
        auname = input("Enter Admin Username : ")
        try:
            res = self.adminServ.GetAdminByUsername(auname)
            if res == []:
                raise AdminNotFoundException
            else:
                print(res)
        except AdminNotFoundException as e:
            print(e)

    def regAdmin(self):
        try:
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
        except ValueError:
            print("Invalid input data. Please enter valid input.")
            return  # Return to prevent further execution
        try:
            self.adminServ.RegisterAdmin(ad)
        except InvalidInputException as e:
            print(e)

    def updateAdmin(self):
        try:
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
        except ValueError:
            print("Invalid input data. Please enter valid input.")
            return  # Return to prevent further execution
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
        print("Exited")

    def run(self):
        while True:
            self.Menu()
            choice = input("Enter your choice: ")
            if choice == "1":
                self.CustomerMenu()
                customer_choice = input("Enter your choice: ")
                if customer_choice == "1":
                    self.authUser()
                elif customer_choice == "2":
                    self.getCustomerByID()
                elif customer_choice == "3":
                    self.regCustomer()
                elif customer_choice == "4":
                    self.updateCustomer()
                elif customer_choice == "5":
                    self.deleteCust()
                elif customer_choice == "6":
                    continue
                else:
                    print("Invalid choice. Please enter a number from 1 to 5.")
            elif choice == "2":
                self.VehicleMenu()
                vehicle_choice = input("Enter your choice: ")
                if vehicle_choice == "1":
                    self.getVehiByID()
                elif vehicle_choice == "2":
                    self.getAvVehi()
                elif vehicle_choice == "3":
                    self.addVehi()
                elif vehicle_choice == "4":
                    self.updateVehi()
                elif vehicle_choice == "5":
                    self.rmVehi()
                elif vehicle_choice == "6":
                    continue
                else:
                    print("Invalid choice. Please enter a number from 1 to 5.")

            elif choice == "3":
                self.ReservationMenu()
                reservation_choice = input("Enter your choice: ")
                if reservation_choice == "1":
                    self.getResByID()
                elif reservation_choice == "2":
                    self.getResByCustID()
                elif reservation_choice == "3":
                    self.createRes()
                elif reservation_choice == "4":
                    self.updateRes()
                elif reservation_choice == "5":
                    self.cancelRes()
                elif reservation_choice == "6":
                    continue
                else:
                    print("Invalid choice. Please enter a number from 1 to 5.")
                    
            elif choice == "4":
                self.AdminMenu()
                admin_choice = input("Enter your choice: ")
                if admin_choice == "1":
                    self.getAdminByID()
                elif admin_choice == "2":
                    self.getAdminByUname()
                elif admin_choice == "3":
                    self.regAdmin()
                elif admin_choice == "4":
                    self.updateAdmin()
                elif admin_choice == "5":
                    self.deleteAdmin()
                elif admin_choice == "6":
                    continue
                else:
                    print("Invalid choice. Please enter a number from 1 to 5.")
            elif choice == "5":
                self.Exit()
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 5.")
            
            option = input("Do you want to continue (Y/N)? ")
            if option.upper() != 'Y':
                self.Exit()
                return


if __name__ == "__main__":
    menu = MainMenu()
    menu.run()




