from IAdminService import IAdminService
from Entity.Admin import Admin
from util.DBPropertyUtil import DBProprtyUtil
from util.DBconnutil import DBconnutil

 

class AdminService(IAdminService):
    def GetAdminById(self,AdminID):
        conn = DBconnutil.getConnection(DBProprtyUtil.getConnectionString('CarConnect'))
        stmt = conn.cursor()
        self.adminid = AdminID
        stmt.execute(f"select * from Admin where AdminID = {self.adminid}")
        row = stmt.fetchall()
        print(row)
        stmt.close()

    def GetAdminByUsername(self,username):
        conn = DBconnutil.getConnection(DBProprtyUtil.getConnectionString('CarConnect'))
        stmt = conn.cursor()
        self.username = username
        stmt.execute(f"select * from admin where Username = '{self.username}'")
        row = stmt.fetchall()
        print(row)
        stmt.close()

    def RegisterAdmin(self,adminData):
        conn = DBconnutil.getConnection(DBProprtyUtil.getConnectionString('CarConnect'))
        stmt = conn.cursor()
        self.admindata = adminData
        stmt.execute(f"insert into Admin values( {self.admindata.getAdminID()},'{self.admindata.getFirstName()}', '{self.admindata.getLastName()}', '{self.admindata.getEmail()}' ,'{self.admindata.getPhoneNumber()}' ,'{self.admindata.getUsername()}','{self.admindata.getPassword()}' ,'{self.admindata.getRole()}','{self.admindata.getJoinDate()}' )")
        conn.commit()
        print("Admin Registered Successfully.")
        stmt.close()

    def UpdateAdmin(self,adminData):
        conn = DBconnutil.getConnection(DBProprtyUtil.getConnectionString('CarConnect'))
        stmt = conn.cursor()
        self.admindata = adminData
        stmt.execute(f" update admin set FirstName = '{self.admindata.getFirstName()}', LastName = '{self.admindata.getLastName()}',Email = '{self.admindata.getEmail()}' ,PhoneNumber = '{self.admindata.getPhoneNumber()}' ,Username = '{self.admindata.getUsername()}',Password = '{self.admindata.getPassword()}' ,Role = '{self.admindata.getRole()}',JoinDate = '{self.admindata.getJoinDate()}' where AdminID = {self.admindata.getAdminID()} )")
        conn.commit() 
        print("Admin updated Successfully")
        stmt.close()

    def DeleteAdmin(self,AdminID):
        conn = DBconnutil.getConnection(DBProprtyUtil.getConnectionString('CarConnect'))
        stmt = conn.cursor()
        self.adminid = AdminID
        stmt.execute(f"Delete from Admin where AdminID = {self.adminid}")
        conn.commit()
        print('Admin deleted successfully')
        stmt.close()
