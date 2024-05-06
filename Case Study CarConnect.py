# Classes:
# • Customer: 
# • Properties: CustomerID, FirstName, LastName, Email, PhoneNumber, Address, 
# Username, Password, RegistrationDate 
# • Methods: Authenticate(password) 
# • Vehicle: 
# • Properties: VehicleID, Model, Make, Year, Color, RegistrationNumber, Availability, 
# DailyRate 
# • Reservation: 
# • Properties: ReservationID, CustomerID, VehicleID, StartDate, EndDate, TotalCost, 
# Status 
# • Methods: CalculateTotalCost() 
# • Admin: 
# • Properties: AdminID, FirstName, LastName, Email, PhoneNumber, Username, 
# Password, Role, JoinDate 
# • Methods: Authenticate(password) 

# • CustomerService (implements ICustomerService): 
# • Methods: GetCustomerById, GetCustomerByUsername, RegisterCustomer, 
# UpdateCustomer, DeleteCustomer 
# • VehicleService (implements IVehicleService): 
# • Methods: GetVehicleById, GetAvailableVehicles, AddVehicle, UpdateVehicle, 
# RemoveVehicle 
# • ReservationService (implements IReservationService): 
# • Methods: GetReservationById, GetReservationsByCustomerId, CreateReservation, 
# UpdateReservation, CancelReservation 
# • AdminService (implements IAdminService): 
# • Methods: GetAdminById, GetAdminByUsername, RegisterAdmin, UpdateAdmin, 
# DeleteAdmin 
# • DatabaseContext: 
# • A class responsible for handling database connections and interactions. 
# • AuthenticationService: 
# • A class responsible for handling user authentication. 
# • ReportGenerator: 
# • A class for generating reports based on reservation and vehicle data. 


import datetime

class Customer:
    def __init__(self):
        self.CustomerID = '', 
        self.FirstName = '',
        self.LastName = '',
        self.Email = '',
        self.PhoneNumber = '',
        self.Address = '', 
        self.Username = '', 
        self.Password = '', 
        self.RegistrationDate = ''

    def getData(self):
        self.CustomerID = int(input('Enter CustomerID : ')), 
        self.FirstName = input('Enter FirstName : '),
        self.LastName = input('Enter LastName : '),
        self.Email = input('Enter Email : '),
        self.PhoneNumber = input('Enter PhoneNumber : '),
        self.Address = input('Enter Address : '), 
        self.Username = input('Enter Username : '), 
        self.Password = input('Enter Password : '), 
        self.RegistrationDate = datetime.strptime(input('Enter RegistrationDate (YYYY-MM-DD): '), '%Y-%m-%d').date()

    def Athenticate(self,Password):
        if self.Password == Password:
            print('Login Successful ')
        else:
            print('TRY AGAIN !!!')

class Vehicle:
    def __init__(self):
        self.VehicleID = '',
        self.Model = '', 
        self.Make = '', 
        self.Year = '',
        self.Color = '',
        self.RegistrationNumber = '',
        self.Availability = '', 
        self.DailyRate = '' 

    def getData(self):
        self.VehicleID = int(input('Enter VehicleID : ')),
        self.Model = input('Enter Model : '), 
        self.Make = input('Enter Make : '), 
        self.Year = datetime.striptime(input('Enter Year (YYYY) : '), '%Y').date(),
        self.Color = input('Enter Color : '),
        self.RegistrationNumber = int(input('Enter RegistrationNumber : ')),
        self.Availability = bool(input('Enter Availability : ')), 
        self.DailyRate = float(input('Enter DailyRate : '))         
