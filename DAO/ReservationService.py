from DAO.IReservationService import IReservationService
from Entity.Reservation import Reservation
from util.DBPropertyUtil import DBProprtyUtil
from util.DBconnutil import DBconnutil
from Exceptions.ReservationException import ReservationException


class ReservationService(IReservationService):
    def GetReservationById(self, reservationId):
        conn = DBconnutil.getConnection(DBProprtyUtil.getConnectionString('CarConnect'))
        stmt = conn.cursor()
        self.resvID = reservationId
        stmt.execute(f"select * from Reservation where ReservationID = {self.resvID}")
        row = stmt.fetchall()
        stmt.close() 
        conn.close()
        return row
    
    def GetReservationsByCustomerId(self, customerId):
        conn = DBconnutil.getConnection(DBProprtyUtil.getConnectionString('CarConnect'))
        stmt = conn.cursor()
        self.custID = customerId
        stmt.execute(f"select * from reservation where CustomerID = {self.custID}") 
        row = stmt.fetchall()
        stmt.close()
        conn.close()
        return row
    
    def CreateReservation(self, reservationData):
        conn = DBconnutil.getConnection(DBProprtyUtil.getConnectionString('CarConnect'))
        stmt = conn.cursor()
        self.resvData = reservationData
    
        try:
            stmt.execute(f"insert into Reservation values({self.resvData.getReservationID()}, {self.resvData.getCustomerID()}, {self.resvData.getVehicleID()}, '{self.resvData.getStartDate()}', '{self.resvData.getEndDate()}', {self.resvData.getTotalCost()}, '{self.resvData.getStatus()}')") 
            conn.commit()
            print("Reservation created Successfully")
        except Exception as e:
            conn.rollback()
            raise ReservationException(f"Error creating reservation: {e}")
        finally:
            stmt.close()
            conn.close()

    
    def UpdateReservation(self, reservationData):
        conn = DBconnutil.getConnection(DBProprtyUtil.getConnectionString('CarConnect'))
        stmt = conn.cursor()
        self.resvData = reservationData
        stmt.execute(f"select * from reservation where ReservationID = {self.resvData.getReservationID()}")
        row = stmt.fetchone()
        if row is None:
            raise ReservationException("Reservation Not Found !!")
        try:
            stmt.execute(f"update Reservation set CustomerID = {self.resvData.getCustomerID()}, VehicleID =  {self.resvData.getVehicleID()}, SatrtDate = '{self.resvData.getStartDate()}', EndDate = '{self.resvData.getEndDate()}', TotalCost = {self.resvData.getTotalCost()}, Status = '{self.resvData.getStatus()}' where ReservationID = {self.resvData.getReservationID()} ") 
            conn.commit()
            print("Reservation Updated Successfully")
        except Exception as e:
            conn.rollback()
            raise ReservationException(f"Error creating reservation: {e}")
        finally:
            stmt.close()
            conn.close()

    def CancelReservation(self, reservationId):
        conn = DBconnutil.getConnection(DBProprtyUtil.getConnectionString('CarConnect'))
        stmt = conn.cursor()
        self.resvID = reservationId
        stmt.execute(f"select * from reservation where ReservationID = {self.resvID}")
        row = stmt.fetchone()
        if row is None:
            raise ReservationException("Reservation Not Found !!")
        try:
            stmt.execute(f"Delete from reservation where ReservationID = {self.resvID}")
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise ReservationException(f"Error creating reservation: {e}")
        finally:
            stmt.close()
            conn.close()
