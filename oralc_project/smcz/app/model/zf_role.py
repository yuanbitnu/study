import os
import sys
project_path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(project_path)
# print(sys.path)
# print(os.path.dirname(__file__))
# print(sys.modules)
from model import pool
from model import logging
from model import oracle
from exception.statuCode import StatuCode
from exception.tools import ToolsHelp


''' 获取角色列表

Returns:
    list | dict -- 返回list角色列表或json格式dict
'''
def getRoles(tableName = None):
    comStr = 'select * from zf_role' # 查询字符串
    try:
        connection = pool.acquire() # 对oracle连接对象池中获取连接
        cursor = connection.cursor() # 获取游标
        cursor.execute(comStr) # 执行SQL语句
        content = cursor.fetchall() # 获取行数据,返回一个元组类型的list列表
        cloumns = cursor.description # 获取当前表查询的列名
        if tableName != None:
            return ToolsHelp.formateData(content,cloumns,tableName) # 调用formateData()工具方法格式化数据
        else:
            return ToolsHelp.formateData(content,cloumns)
    except oracle.DatabaseError as msg:
        logging.info(msg)
        return StatuCode.selectTabelError.value
    except Exception as e:
        logging.info(e)
        return StatuCode.unknowError.value
    finally:
        cursor.close() # 关闭游标
        pool.release(connection) # 释放连接对象回连接池

def insertRole(roleName):
    comStr = 'insert into zf_role (r_name) values (:roleName)' # 带参数的插入语句
    try:
        connection = pool.acquire()
        cursor = connection.cursor()
        cursor.execute(comStr,(roleName,)) # 带参数的执行语句
        connection.commit() # 通过连接对象提交
        return StatuCode.successCode.value
    except oracle.DatabaseError as msg:
        logging.info(msg)
        return StatuCode.insertDataError.value
    except Exception as e:
        logging.info(e)
        return StatuCode.unknowError.value
    finally:
        cursor.close() # 关闭游标
        pool.release(connection) # 释放连接对象回连接池

def delRoles(id:int = None,roleName:str = None): 
    comStr = ''
    paramers = None
    if id == None and roleName != None:
        comStr = 'delete from zf_role where r_name = :arg'
        paramers = (roleName,)
    elif id !=None and roleName == None:
        comStr = 'delete from zf_role where r_id = :arg'
        paramers = (id,)
    elif id != None and roleName != None:
        comStr = 'delete from zf_role where r_id = :id and r_name = :roleName'
        paramers = (id,roleName)
    else:
        logging.info('未指定查询语句')
    try:
        connection = pool.acquire()
        cursor = connection.cursor()
        cursor.execute(comStr,paramers) # 带参数的执行语句
        connection.commit() # 通过连接对象提交
        return StatuCode.successCode.value
    except oracle.DatabaseError as msg:
        logging.info(msg)
        return StatuCode.deleteDataError.value
    except Exception as e:
        logging.info(e)
        return StatuCode.unknowError.value
    finally:
        cursor.close() # 关闭游标
        pool.release(connection) # 释放连接对象回连接池
    
def updateRole(id,newRoleName):
    comStr = 'update zf_role t set t.r_name = :name where t.r_id = :id' # 更新语句
    try:
        connection = pool.acquire()
        cursor = connection.cursor()
        cursor.execute(comStr,{'name':newRoleName,'id':id}) # 参数为dict的执行语句,通过key匹配值
        connection.commit() # 通过连接对象提交
        return StatuCode.successCode.value
    except oracle.DatabaseError as msg:
        logging.info(msg)
        return StatuCode.insertDataError.value
    except Exception as e:
        logging.info(e)
        return StatuCode.unknowError.value
    finally:
        cursor.close() # 关闭游标
        pool.release(connection) # 释放连接对象回连接池


if __name__ == "__main__":
    # insertRole('出纳3')
    # res = getRoles()
    # print(res)
    # delRoles(roleName='出纳3')
    # updateRole(3,'出纳2')
    res = getRoles()
    print(res)