import os
import sys
import time
import datetime
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

def getUkeys(tableName = None):
    comStr = 'select * from zf_ukey' # 查询字符串
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

def insertUkey(id:int,Name:str,Mobile:str,CarNum:str,CompanyId:int,roleId:int):
    comStr = 'insert into zf_Ukey u (u.ukey_id,u.ownername,u.ownermobil,u.ownercarnum,u.ownercompanynum,u.role_id) values (:ukeyID,:ownName,:ownMobil,:ownCarNum,:ownCompanyNum,:roleId)' # 带参数的插入语句
    try:
        connection = pool.acquire()
        cursor = connection.cursor()
        cursor.execute(comStr,{'ukeyID':id,'ownName':Name,'ownMobil':Mobile,'ownCarNum':CarNum,'ownCompanyNum':CompanyId,'roleId':roleId}) # 带参数的执行语句
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

def delUkey(id:int): 
    comStr = 'delete from zf_ukey where ukey_id = :id'
    paramers = (id,)
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
    
# def updateUkey(id:int,phoneNum:str=None,companuId:int=None,useTiem:float=None,unuseTime:float=None):
#     comStr = 'update zf_ukey t set t.mc_name = :name where t.mc_id = :id' # 更新语句
#     try:
#         connection = pool.acquire()
#         cursor = connection.cursor()
#         cursor.execute(comStr,{'name':newMcName,'id':id}) # 参数为dict的执行语句,通过key匹配值
#         connection.commit() # 通过连接对象提交
#         return StatuCode.successCode.value
#     except oracle.DatabaseError as msg:
#         logging.info(msg)
#         return StatuCode.insertDataError.value
#     except Exception as e:
#         logging.info(e)
#         return StatuCode.unknowError.value
#     finally:
#         cursor.close() # 关闭游标
#         pool.release(connection) # 释放连接对象回连接池


if __name__ == "__main__":
    # ret = insertUkey('经济建设股')
    # ret = updateUkey(8,'石门县住保办')
    # ret = delUkey('石门县主板宝')
    # ret = delUkey(ManageCompanyName='石门县住保办')
    # res = getUkeys('zf_ukey')
    # print(res)
    res = time.time()
    res = datetime.datetime.now()
    print(res,type)