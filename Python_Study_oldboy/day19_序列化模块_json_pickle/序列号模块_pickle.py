# pickle序列化模块,基本上和json模块功能一样,但它不涉及和其他编程语言交换数据,因此它可序列号的类型几乎是所有python支持的数据类型
# pickle模块和json模块会将对象序列化成bytes字节,而json模块是将对象序列号为json字符串
import pickle

# 一.pickle模块提供的方法

# 1.序列化和反序列化到内存中一对方法
# pickle.dumps(),将对象序列化成字节,dict(字典的key也可以为int),set,tuple,string,int,list都可以进行序列化
# pickle.loads(),将字节串反序列化
# lis = [{'name': '张三', 'age': 18, 'hobby': (
#     'eat', 'draw', 'run'), 'book': {'世界简史', '未来简史'}}, ]
# ret = pickle.dumps(lis)
# print(ret, type(ret))  # result = f\xb2q\x0ee\x85q\x0fRq\x10ua.' <class 'bytes'>

# ret1 = pickle.loads(ret)
# print(ret1, type(ret1)) # result = [{'name': '张三', 'age': 18, 'hobby': ('eat', 'draw', 'run'), 'book': {'未来简史', '世界简史'}}] <class 'list'>


# 2.直接序列化和反序列化到文件中的一对方法

# lis = [{'name': '张三', 'age': 18, 'hobby': (
#     'eat', 'draw', 'run'), 'book': {'世界简史', '未来简史'}}, ]
# with open('pickle_seliz', mode='ab') as file_stream:  #因为序列化后的内容是bytes,因此mode = 'ab',同时不需要指定编码
#     pickle.dump(lis, file_stream)

# with open('pickle_seliz',mode = 'rb') as file_stream:
# 	ret = pickle.load(file_stream)
# 	print(ret)


# 二.pickle模块和json模块不一样的还有pickle模块可以多次反序列化对应的多次序列化对象
# lis = [{'name': '张三', 'age': 18, 'hobby': (
#     'eat', 'draw', 'run'), 'book': {'世界简史', '未来简史'}}, ]
# with open('pickle_seliz', mode='ab') as file_stream:  # 序列化多个对象到文件
#     pickle.dump(lis, file_stream)
#     pickle.dump(lis, file_stream)
#     pickle.dump(lis, file_stream)

# with open('pickle_seliz', mode='rb') as file_stream:
#     ret = pickle.load(file_stream)
#     print(ret)

#     ret = pickle.load(file_stream)
#     print(ret)

#     ret = pickle.load(file_stream)
#     print(ret)

# ret = pickle.load(file_stream) #文件内容反序列化完了以后继续反序列化会抛出EOFError异常
# print(ret)

with open('pickle_seliz', mode='rb') as file_stream:
    while True:
        try:
            ret = pickle.load(file_stream)
            print(ret)
        except EOFError:
            break
