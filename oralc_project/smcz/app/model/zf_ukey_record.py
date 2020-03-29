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

def getUkeyRecords():
    comStr = 'select * from zf_ukey_record' # 查询字符串
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

def insertUkeyRecord(recordObj):
    comStr = "insert into zf_ukey_record (ur_company_num,ur_role_num,ur_ukey_num,ur_action_num,ur_proposer,ur_application_content,ur_create_time) values (:companyNum,:roleNum,:ukeyNum,:actionNum,:propName,:applicontent,:createTime)" # 带参数的插入语句
    paramers = {'companyNum':recordObj.companyNum,'roleNum':recordObj.roleNum,'ukeyNum':recordObj.ukeyNum,'actionNum':recordObj.actionNum,'propName':recordObj.proposerName,'applicontent':recordObj.applicationContent,'createTime':recordObj.createTime}
    try:
        connection = pool.acquire()
        cursor = connection.cursor()
        cursor.execute(comStr,paramers) # 带参数的执行语句
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
    time = ToolsHelp.getCurrentTime()
    # res = insertUkeyRecord(1,2,4002,'李四','ukey遗失,重新补办',time,'李四')
    res = getUkeyRecords()
    print(res)