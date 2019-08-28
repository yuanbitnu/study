# time模块,关于时间操作的模块:
# 一.时间格式:
# 字符串时间: '2018-8-20','2018.08.20'  给用户看的
'''结构化时间: time.struct_time(tm_year=2019, tm_mon=6, tm_mday=17, tm_hour=10,
tm_min=53, tm_sec=45, tm_wday=0, tm_yday=168, tm_isdst=0)  介于字符串时间和时间戳时间之间的一个结构化类型'''
# 浮点型时间: 1560739772.8115404  给机器看到，一秒为单位，从1970年1月1日 00:00:00开始

import time

# # 时间戳时间 Timestamp
# print(time.time())


# # /元组时间结构化时间(time.struct_time)
# print(time.localtime())


# # 格式化时间
# print(time.strftime('%Y-%m-%d'))

# 二.时间格式的转换
# 1.从时间戳时间转换为格式化时间(不能直接转,需要经过结构化时间)
# localtime显示结构化北京时间,gmtime()显示伦敦结构化时间，不传参数表示当前时间
struct_time = time.localtime()
london_struct_time = time.gmtime()
#
# 使用localtime()或gmtime()传入一个时间戳,将该时间戳转化为结构化时间
struct_time = time.localtime(15000000000)
london_struct_time = time.gmtime(15000000000)

# 使用strftime()将结构化时间格式化为格式化时间
format_time = time.strftime("%Y/%m/%d", struct_time)
london_format_time = time.strftime("%Y/%m/%d", struct_time)
# 打印格式化时间结果
print(format_time)
print(london_format_time)

# 2.从格式化时间转为时间戳时间(不能直接转，需要经过结构化时间)

# 使用strptime方法将格式化时间转为结构化时间
struct_time = time.strptime('2017-2-14', '%Y-%m-%d')

# 使用mktime方法将结构化时间转为时间戳时间
time_stamp = time.mktime(struct_time)

# 打印时间戳时间
print(time_stamp)
