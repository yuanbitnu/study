# json 一种轻量级的数据交换格式，可以在不同的编程语言之间进行数据交换
# json模块 用于将python中的数据类型序列化成json格式，或者反序列化为原始格式，以便方便数据的交换和使用
# json数据格式因为需要在不同的编程语言之间进行数据交换，因此json模块支持的数据类型是有限的：字符串，列表，字典(字典中的key必须是字符串)，数字
# json模块可以练习多次序列化，但在反序列化的时候 一次只能反序列化一个完整的字符串对象，如果有多次序列化的内容，需要分别读出来后进行反序列化
import json
# 一、json模块提供的方法

# 1. 在内存中序列化和反序列化的一对方法
# json.dumps(),在内存中序列化一个对象成json格式的字符串
# json.loads(),在内存中反序列化一个json格式的字符串
# dic = {'key_one': 'value_one', 'key_two': 'value_two'}
# ret = json.dumps(dic)
# # result = {"key_one": "value_one", "key_two": "value_two"} <class 'str'>
# print(ret, type(ret))

# ret1 = json.loads(ret)
# print(ret1, type(ret1)) #result = {'key_one': 'value_one', 'key_two': 'value_two'} <class 'dict'>


# 2.直接序列化到文件和从文件反序列化到内存中的一对方法
# json.dump(),直接将序列化的内容写入到文件中
# json.load(),直接从文件反序列化到内存

# dic = {'key_one': 'value_one', 'key_two': 'value_two', "张三": 19}
# with open('json_serliz', mode='a', encoding='utf-8') as file_stream:
#     # json.dump(dic, file_stream)  # result = {"key_one": "value_one", "key_two": "value_two", "\u5f20\u4e09": 19} 将序列化的内容写入文件，中文会以编码显示
#     json.dump(dic,file_stream,ensure_ascii = False) # result = {"key_one": "value_one", "key_two": "value_two", "张三": 19} 中文显示正常


# with open('json_serliz', mode='r', encoding='utf-8') as file_stream:
#     ret = json.load(file_stream)
#     print(ret) #result = {'key_one': 'value_one', 'key_two': 'value_two', '张三': 19}


# 二、反序列化的时候 一次只能反序列化一个完整的字符串对象
# dic = {'key_one': 'value_one', 'key_two': 'value_two', "张三": 19}
# with open('json_serliz',mode = 'a',encoding = 'utf-8') as file_stream:
#   json_ret = json.dumps(dic) + '\n'
#   file_stream.write(json_ret)

#   json_ret = json.dumps(dic) + '\n'
#   file_stream.write(json_ret)

#   json_ret = json.dumps(dic) + '\n'
#   file_stream.write(json_ret)     #连续3次序列化并写入文件


# with open('json_serliz', mode='r', encoding='utf-8') as file_stream:
#     for line in file_stream:
#         ret = json.loads(line)
#         print(ret)  # 分次从文件读取对象并反序列化到内存
