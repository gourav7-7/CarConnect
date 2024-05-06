import mysql.connector as sql
from util.DBPropertyUtil import DBProprtyUtil
from util.DBconnutil import DBconnutil

class DatabaseContext:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn_str = DBProprtyUtil.getConnectionString(db_name)
        self.conn = DBconnutil.getConnection(self.conn_str)
        self.stmt = self.conn.cursor()

    def close_connection(self):
        self.stmt.close()
        self.conn.close()

    def runQuery(self, query):
        self.stmt.execute(query)
        result = self.stmt.fetchall()
        return result


