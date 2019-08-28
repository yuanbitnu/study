import logging
# https://cloud.tencent.com/developer/article/1354396


'''
logging中的几种 Python 类型，Logger、LogRecord、Filter、Handler、Formatter。
类型说明：
Logger：日志，暴露函数给应用程序，基于日志记录器和过滤器级别决定哪些日志有效。
LogRecord ：日志记录器，将日志传到相应的处理器处理。
Handler ：处理器, 将(日志记录器产生的)日志记录发送至合适的目的地。
Filter ：过滤器, 提供了更好的粒度控制,它可以决定输出哪些日志记录。
Formatter：格式化器, 指明了最终输出中日志记录的布局。
'''

#  一、logging 的基本使用(使用basicConfig())

'''filename   日志输出到文件的文件名
   filemode   文件模式，r[+]、w[+]、a[+]
   format   日志输出的格式
   datefat   日志附带日期时间的格式
   style   格式占位符，默认为 "%" 和 “{}”
   level   设置日志输出级别
   stream   定义输出流，用来初始化 StreamHandler 对象，不能 filename 参数一起使用，否则会ValueError 异常
   handles   定义处理器，用来创建 Handler 对象，不能和 filename 、stream 参数一起使用，否则也会抛出 ValueError 异常
'''
# logging.basicConfig(filename="test.log", filemode="w", format="%(asctime)s %(name)s:%(levelname)s:%(message)s",
#                     datefmt="%d-%M-%Y %H:%M:%S", level=logging.ERROR)
# # logging.basicConfig(level=logging.ERROR)
# logging.debug('this is debug message')
# logging.info('this is info message')
# logging.warning('this is warning message')
# logging.error('this is error message')
# logging.critical('this is cirtical message')

# 二、使用logging模块输出try..Exception 异常信息

# 中文乱码问题的解决
# 一、在basicConfig()配置中使用handlers列表参数，在其中创建一个Filehandler对象，指定encoding编码为“utf-8”
# 二、自定义logger对象中的handler（）
#   1、handler = logging.FileHandler(filename="test.log", encoding="utf-8")
#   2.logger.addHandler(handler)


# logging.basicConfig(handlers=[logging.FileHandler('test_two.log', encoding='utf-8')], format="%(asctime)s %(name)s:%(levelname)s:%(message)s",
#                     datefmt="%d-%M-%Y %H:%M:%S", level=logging.ERROR)
# a = 5
# b = 0
# try:
#     c = a / b
# except Exception as e:
#     logging.exception('hhh')  # 方式一
#     logging.error('Error 除数不能为0', exc_info=True)  # 方式二、必须将exc_info 设置为True

#     logging.log(level=logging.ERROR, msg='Log除数不能为0', exc_info=True) # 方式三、必须设置日志级别以及exc_info 必须设为True


# 三、自定义logger，自定义handler处理器、formatter格式化器、一个程序系统只有一个root(根)logger，并且该类不能通过直接实例化产生对象，在该类中使用了单列模式
# 因此Logger对象的获取只能使用getLogger()方法

# 1.获取logger对象
# 获取根 logger对象,参数为根logger名称，默认为root
# logger = logging.getLogger('tyb')  # 10-55-2019 16:55:45 tyb ERROR This is an customer error message
# 10-57-2019 16:57:22 root ERROR This is an customer error message
logger = logging.getLogger()

# 2.创建handler处理器对象,如果想要分别输出到不同的记录对象中(比如控制台和文件)，则可以创建两个不同的handler处理器
handler_one = logging.StreamHandler()  # 创建一个StreamHandler流处理器对象,输出到控制台
handler_two = logging.FileHandler(
    'test_three.log', mode='a', encoding='utf-8')  # 创建一个FileHandler文件处理器对象，输出到文件

# 3.为logger、handler设置level日志级别
# logger中的level是全局允许的最低级别,任何handler处理器中level低于logger level级别的handler处理器都将不会生效不会被记录
logger.setLevel(logging.ERROR)  # logger对象可以设置日志级别
handler_one.setLevel(logging.DEBUG)  # handler也可以设置日志级别
handler_two.setLevel(logging.WARNING)  # 只有比logger级别高的level才会被记录

# 4.创建Formatter格式化器
formatter_one = logging.Formatter(
    fmt="%(asctime)s %(name)s %(levelname)s %(message)s", datefmt="%d-%M-%Y %H:%M:%S")  # 创建一个带时间格式化的formatter格式化器
formatter_two = logging.Formatter(
    fmt="%(asctime)s %(name)s %(levelname)s %(message)s")  # 创建一个不带时间格式化的formatter格式化器

# 5.为处理器添加formatter格式化器
handler_one.setFormatter(formatter_one)  # 为handler处理器设置Formatter格式化器
handler_two.setFormatter(formatter_two)  # 为handler处理器设置Formatter格式化器

# 6.为logger对象添handler处理器,一个logger可以添加多个handler处理器，在basicConfig()中可以设置 handlers(处理器列表)添加多个handler处理器
logger.addHandler(handler_two)
logger.addHandler(handler_one)

print(logger.level)  # level = 10
print(handler_one.level)  # level = 40
print(handler_two.level)  # level = 30

logger.debug('This is a customer debug message')
logger.info('This is an customer info message')
logger.warning('This is a customer warning message')
logger.error('This is an customer error message')
logger.critical('This is a customer critical message')
