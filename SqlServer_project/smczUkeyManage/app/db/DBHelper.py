import pymssql
import os

class DBHelper:
    
    def __init__(self,host = '127.0.0.1',port = '1433',user = 'sa',password = 'Xxzx.5155932',database = 'UkeyDB',as_dicct = True):
        try:
            self.conn = pymssql.connect(host,user,password,database)
            self.cursor = self.conn.cursor()
        except Exception as e:
            print(e)
            
    def ExecQuery(self,sql)