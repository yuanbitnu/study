import logging
''' 创建logger对象
'''
logger = logging.getLogger('oracleError')
''' 创建logger handler,将日志输出到文件
'''
handlerFile = logging.FileHandler('../logText.log',mode='a',encoding='utf-8')

''' 设置日志记录的级别
'''
logger.setLevel(logging.INFO)

''' 创建带时间格式化的格式化器
'''
formatter = logging.Formatter(fmt="%(asctime)s %(name)s %(levelname)s %(message)s", datefmt="%m-%d-%Y %H:%M:%S")

''' 将格式化器添加到处理器
'''
handlerFile.setFormatter(formatter)

''' 将处理器添加进logger对象
'''
logger.addHandler(handlerFile)
