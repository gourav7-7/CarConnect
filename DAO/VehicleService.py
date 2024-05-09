from DAO.IVheicleService import IVehicleService
from Entity.Vehicle import Vehicle
from util.DBPropertyUtil import DBProprtyUtil
from util.DBconnutil import DBconnutil
from Exceptions.VehicleNotFoundException import VehicleNotFoundException



class VehicleService(IVehicleService):
    def GetVehicleById(self, vehicleId):
        conn = DBconnutil.getConnection(DBProprtyUtil.getConnectionString('CarConnect'))
        stmt = conn.cursor()
        self.vehicleid = vehicleId
        stmt.execute(f"select * from Vehicle where VehicleID = {self.vehicleid}")
        row = stmt.fetchall()
        stmt.close()
        return row
    
    def GetAvailableVehicles(self):
        conn = DBconnutil.getConnection(DBProprtyUtil.getConnectionString('CarConnect'))
        stmt = conn.cursor()
        stmt.execute(f"select * from vehicle where Availability = 1")
        row = stmt.fetchall()
        stmt.close()
        if row:
            return True
        else:
            return False
        
    def GetAllVehicles(self):
        conn = DBconnutil.getConnection(DBProprtyUtil.getConnectionString('CarConnect'))
        stmt = conn.cursor()
        stmt.execute(f"select * from vehicle")
        row = stmt.fetchall()
        if row:
            for i in row:
                print(i)
            return True
        stmt.close()


    def AddVehicle(self,vehicleData):
        conn = DBconnutil.getConnection(DBProprtyUtil.getConnectionString('CarConnect'))
        stmt = conn.cursor()
        self.vehicleData = vehicleData
        stmt.execute(f"insert into vehicle values({self.vehicleData.getVehicleID()},'{self.vehicleData.getModel()}','{self.vehicleData.getMake()}',{self.vehicleData.getYear()},'{self.vehicleData.getColor()}','{self.vehicleData.getRegistrationNumber()}',{self.vehicleData.getAvailability()},{self.vehicleData.getDailyRate()})") 
        conn.commit()
        print("Vehicle Added Successfully")
        stmt.close()

    def UpdateVehicle(self, vehicleData):
        conn = DBconnutil.getConnection(DBProprtyUtil.getConnectionString('CarConnect'))
        stmt = conn.cursor()
        self.vehicleData = vehicleData
        stmt.execute(f"select * from vwhicle where VehicleID = {self.vehicleid}")
        exists = stmt.fetchone()
        if exists is None:
            stmt.close()
            conn.close()
            raise VehicleNotFoundException()
        stmt.execute(f"UPDATE vehicle SET Model='{self.vehicleData.getModel()}', Make='{self.vehicleData.getMake()}', Year={self.vehicleData.getYear()}, Color='{self.vehicleData.getColor()}', RegistrationNumber='{self.vehicleData.getRegistrationNumber()}', Availability={self.vehicleData.getAvailability()}, DailyRate={self.vehicleData.getDailyRate()} WHERE VehicleID={self.vehicleData.getVehicleID()}")
        conn.commit()
        print("Vehicle Updated Successfully")
        stmt.close()

    def RemoveVehicle(self,vehicleID):
        conn = DBconnutil.getConnection(DBProprtyUtil.getConnectionString('CarConnect'))
        stmt = conn.cursor()
        self.vehicleid = vehicleID
        stmt.execute(f"select * from vwhicle where VehicleID = {self.vehicleid}")
        exists = stmt.fetchone()
        if exists is None:
            stmt.close()
            conn.close()
            raise VehicleNotFoundException()
        stmt.execute(f"delete from vehicle where VehicleID = {self.vehicleid}")
        conn.commit()
        print("Vehicle removed")
        stmt.close()
