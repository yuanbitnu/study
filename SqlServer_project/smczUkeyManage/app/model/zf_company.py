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


def getCompanys():
    comStr = 'select * from zf_companys'
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

def getCompanysByLevel(levelId:int,companys):
    companysByLevel =[]
    for item in companys:
        if item['levelid'] == levelId:
            companysByLevel.append(item)
    return companysByLevel

def getcompanyTree():
    companys = getCompanys()
    lev_one = getCompanysByLevel(1,companys)
    lev_two = getCompanysByLevel(2,companys)
    lev_three = getCompanysByLevel(3,companys)
    if type(lev_one) == list and type(lev_two) == list and type(lev_three) == list:
        for twoItem in lev_two:
            twoItem.update({"children":[]})
            for threeItem in lev_three:
                threeItem.update({"children":[]})
                if threeItem['pid'] == twoItem['compid']:
                    twoItem['children'].append(threeItem)
        for oneItem in lev_one:
            oneItem.update({"children":[]})
            for twoItem in lev_two:
                if twoItem['pid'] == oneItem['compid']:
                    oneItem['children'].append(twoItem)
        return [{"compid":0,"compname":"石门县","pid":-1,"levelid":0,"children":lev_one}]
    else:
        return StatuCode.errorCode.value

if __name__ == "__main__":
    res = getcompanyTree()
    print(res)