from DAO.IReservationService import IReservationService
from Entity.Reservation import Reservation
from util.DBPropertyUtil import DBProprtyUtil
from util.DBconnutil import DBconnutil

conn_str = DBProprtyUtil.getConnectionString('CarConnect')
conn = DBconnutil.getConnection(conn_str)
stmt = conn.cursor()

class ReservationService(IReservationService):
    def GetReservationById(self, reservationId):
        self.resvID = reservationId
        stmt.execute(f"select * from Reservation where ReservationID = {self.resvID}")
        row = stmt.fetchall()
        print(row)
        stmt.close() 
    
    def GetReservationsByCustomerId(self, customerId):
        self.custID = customerId
        stmt.execute(f"select * from reservation where CustomerID = {self.custID}") 
        row = stmt.fetchall()
        print(row)
        stmt.close()
    
    def CreateReservation(self, reservationData):
        self.resvData = reservationData
        stmt.execute(f"insert into Reservation values({self.resvData.getReservationID()}, {self.resvData.getCustomerID()}, {self.resvData.getVehicleID()}, '{self.resvData.getStartDate()}', '{self.resvData.getEndDate()}', {self.resvData.getTotalCost()}, '{self.resvData.getStatus()}')") 
        conn.commit()
        print("Reservation created Successfully")
        stmt.close()
    
    def UpdateReservation(self, reservationData):
        self.resvData = reservationData
        stmt.execute(f"update Reservation set CustomerID = {self.resvData.getCustomerID()}, VehicleID =  {self.resvData.getVehicleID()}, SatrtDate = '{self.resvData.getStartDate()}', EndDate = '{self.resvData.getEndDate()}', TotalCost = {self.resvData.getTotalCost()}, Status = '{self.resvData.getStatus()}' where ReservationID = {self.resvData.getReservationID()} ") 
        conn.commit()
        print("Reservation Updated Successfully")
        stmt.close()

    def CancelReservation(self, reservationId):
        self.resvID = reservationId
        stmt.execute(f"Delete reservation where ReservationID = {self.resvID}")
        conn.commit()
        stmt.close()
