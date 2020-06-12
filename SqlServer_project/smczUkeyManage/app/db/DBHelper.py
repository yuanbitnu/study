import pymssql
from DBUtils.PooledDB import PooledDB

class DBHelper:
    
    def __init__(self,host,port,user,password,database,as_dicta):
        try:
            self.Pool = PooledDB(creator = pymssql,mincached = 2,maxcached = 5,maxshared = 3,maxconnections = 6,blocking = True,\
                host= host,port = port,user = user,password = password,database = database,charset = 'utf8')
        except Exception as e:
            print(e)
            
    def Getcursor(self):
        try:
            self.conn = self.Pool.connection()
            cur = self.conn.cursor()
            if not cur:
                raise '数据库连接不上'
            else:
                return cur
        except Exception as e:
            print(e)
            
    def ExecQuery(self,sqlcom):
        cur = self.Getcursor()
        cur.execcut(sqlcom)
        dic = cur.fetchall()
        cur.close()       
        self.conn.close()
        return dic