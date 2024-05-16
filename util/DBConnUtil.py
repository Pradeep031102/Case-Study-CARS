import pyodbc
from util.DBPropertyUtil import DBPropertyUtil

class DBConnUtil:
    connection = None

    @staticmethod
    def getConnection():
        if DBConnUtil.connection is None:
            connection_string = DBPropertyUtil.getPropertyString('db.properties')
            DBConnUtil.connection = pyodbc.connect(connection_string)
        return DBConnUtil.connection
