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

def getManageCompanys():
    comStr = 'select * from zf_manage_company' # 查询字符串
    try:
        connection = pool.acquire() # 对oracle连接对象池中获取连接
        cursor = connection.cursor() # 获取游标
        cursor.execute(comStr) # 执行SQL语句
        content = cursor.fetchall() # 获取行数据,返回一个元组类型的list列表
        cloumns = cursor.description # 获取当前表查询的列名
        return ToolsHelp.formateData(content,cloumns) # 调用formateData()工具方法格式化数据
    except oracle.DatabaseError as msg:
        logging.info(msg)
        return StatuCode.selectTabelError.value
    except Exception as e:
        logging.info(e)
        return StatuCode.unknowError.value
    finally:
        cursor.close() # 关闭游标
        pool.release(connection) # 释放连接对象回连接池

def insertManageCompany(McName):
    comStr = 'insert into zf_manage_company (mc_name) values (:name)' # 带参数的插入语句
    try:
        connection = pool.acquire()
        cursor = connection.cursor()
        cursor.execute(comStr,{'name':McName}) # 带参数的执行语句
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

def delManageCompany(id:int = None,ManageCompanyName:str = None): 
    comStr = ''
    paramers = None
    if id == None and ManageCompanyName != None:
        comStr = 'delete from zf_manage_company where mc_name = :arg'
        paramers = (ManageCompanyName,)
    elif id !=None and ManageCompanyName == None:
        comStr = 'delete from zf_manage_company where mc_id = :arg'
        paramers = (id,)
    elif id != None and ManageCompanyName != None:
        comStr = 'delete from zf_manage_company where mc_id = :id and mc_name = :name'
        paramers = {'id':id,'name':ManageCompanyName}
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
    
def updateManageCompany(id,newMcName):
    comStr = 'update zf_manage_company t set t.mc_name = :name where t.mc_id = :id' # 更新语句
    try:
        connection = pool.acquire()
        cursor = connection.cursor()
        cursor.execute(comStr,{'name':newMcName,'id':id}) # 参数为dict的执行语句,通过key匹配值
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
    ret = insertManageCompany('经济建设股')
    # ret = updateManageCompany(8,'石门县住保办')
    # ret = delManageCompany('石门县主板宝')
    ret = delManageCompany(ManageCompanyName='石门县住保办')
    res = getManageCompanys()
    print(res,ret)