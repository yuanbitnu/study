import cx_Oracle as oracle
import logging
logging.basicConfig(handlers=[logging.StreamHandler(),logging.FileHandler(
    filename = 'logText.log', mode='a+', encoding='utf-8')], format="%(asctime)s %(name)s:%(levelname)s:%(message)s",datefmt="%m-%d-%Y %H:%M:%S",level=logging.INFO)

''' 获取oracle连接池对象
'''
try:
    pool = oracle.SessionPool(user='xxzx',password='Xxzx5155932',dsn='127.0.0.1/smczxx',encoding = 'UTF-8')
except oracle.DatabaseError as msg:
    logging.info(msg) # 获取失败则写入日志
except Exception as e:
    logging.info(e.args)


