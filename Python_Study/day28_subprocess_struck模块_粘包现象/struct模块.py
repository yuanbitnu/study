import struct

# ********struct模块********
# https://www.cnblogs.com/caodneg7/p/9485137.html

# 1.按照指定格式将Python数据转换为字符串,该字符串为字节流,如网络传输时,不能传输int,此时先将int转化为字节流,然后再发送;
# 2.按照指定格式将字节流转换为Python指定的数据类型;
# 3.处理二进制数据,如果用struct来处理文件的话,需要用’wb’,’rb’以二进制(字节流)写,读的方式来处理文件;
# 4.处理c语言中的结构体;


# 函数                                        return              explain
# pack(fmt,v1,v2…)                            string              按照给定的格式(fmt),把数据转换成字符串(字节流),并将该字符串返回.
# pack_into(fmt,buffer,offset,v1,v2…)         None                按照给定的格式(fmt),将数据转换成字符串(字节流),并将字节流写入以offset开始的buffer中.(buffer为可写的缓冲区,可用array模块)
# unpack(fmt,v1,v2…..)                        tuple               按照给定的格式(fmt)解析字节流,并返回解析结果
# pack_from(fmt,buffer,offset)                tuple               按照给定的格式(fmt)解析以offset开始的缓冲区,并返回解析结果
# calcsize(fmt)                               size of fmt         计算给定的格式(fmt)占用多少字节的内存，注意对齐方式


# 当打包或者解包的时,需要按照特定的方式来打包或者解包.该方式就是格式化字符串,
# 它指定了数据类型,除此之外,还有用于控制字节顺序、大小和对齐方式的特殊字符.

# 格式符

# 格式符       C语言类型               Python类型        Standard size
# x         pad byte(填充字节)  no value
# c         char                string of length 1      1
# b         signed char         integer                 1
# B         unsigned char       integer                 1
# ?         _Bool               bool                    1
# h         short               integer                 2
# H         unsigned short      integer                 2
# i         int                 integer                 4
# I(大写的i)   unsigned int        integer                 4
# l(小写的L)   long                integer                 4
# L         unsigned long       long                    4
# q         long long           long                    8
# Q         unsigned long long  long                    8
# f         float               float                   4
# d         double              float                   8
# s         char[]              string
# p         char[]              string
# P         void *              long
# 注- -!

# _Bool在C99中定义,如果没有这个类型,则将这个类型视为char,一个字节;
# q和Q只适用于64位机器;
# 每个格式前可以有一个数字,表示这个类型的个数,如s格式表示一定长度的字符串,4s表示长度为4的字符串;4i表示四个int;
# P用来转换一个指针,其长度和计算机相关;
# f和d的长度和计算机相关;


# 对齐方式
# Character     Byte order      Size    Alignment
# @(默认)     本机              本机      本机,凑够4字节
# =             本机              标准      none,按原字节数
# <              小端              标准      none,按原字节数
# >              大端              标准      none,按原字节数
# !             network(大端) 标准      none,按原字节数

# 一、字符串
# 字符串文本必须是字节流,如果是英文则在字符串前面加"b",如果是中文则必须进行encode()
# record = '今天天气好晴朗处处好风光'.encode('utf-8')
# l = len(record)  # 计算编码后的字节数
# print(l)  # 36
# ret = struct.unpack('<%ds' % l, record)  # 如果value参数为字符串文本,则必须是字节流,返回一个元组
# print(ret[0].decode(encoding='utf-8'))

# print(struct.calcsize('36s'))  # result = 36


# 二、数字
num = 123456

ret = struct.pack('i', num)
print(ret)  # result = b'8\x00\x00\x00'

# num_two = struct.unpack('i', ret)  # 返回一个元组
# print(num_two[0], type(num_two[0]))  # result = 56 <class 'int'>
