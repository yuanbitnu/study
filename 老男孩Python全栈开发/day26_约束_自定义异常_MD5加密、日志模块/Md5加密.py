import hashlib

# 使用MD5时针对简单明文的加密为了防止暴力破解，可以在加密过程中添加一段自定义字符串(盐)与需要加密的明文一起进行加密

salt = b'tyb'  # md5加密过程中的“盐”
mdobj = hashlib.md5(salt)  # 实例化MD5对象的时候将需要加的盐作为参数传递进去

# 将需要加密的内容作为参数传递进update()方法中，python中该参数必须是字节，使用b'',或encode()
mdobj.update(b'hhhhhhhhhh')

md5_after = mdobj.hexdigest()  # 以十六进制数返回报文摘要结果
print(md5_after)


# 注意，如果一个md5对象练习update()多个字符串内容得到的结果等同于一个md5对象对该字符串分开update()
# 一、
mdobj_one = hashlib.md5()
mdobj_one.update(b'helloWorld')
ret = mdobj_one.hexdigest()
print(ret)  # result = 1a833da63a6b7e20098dae06d06602e1

# 二、
mdobj_two = hashlib.md5()
mdobj_two.update(b'hello')
mdobj_two.update(b'World')
ret = mdobj_two.hexdigest()
print(ret)  # result = 1a833da63a6b7e20098dae06d06602e1


# 应用场景：当一个文件很大时，不可能一次性的完全读人内存进行MD5加密，因此可以分批次的读入内存使用MD5中update()方法进行连续加密

md5 = hashlib.md5()
with open('选课系统(反射).py', mode='rb') as file_stream:
    full_data = file_stream.read()  # 将文件一次性读入内存
    md5.update(full_data)
    ret = md5.hexdigest()  # result = e4e372d8cbca4b48c79d5c820a517656
    print(ret)


md5_two = hashlib.md5()
with open('选课系统(反射).py', mode='rb') as file_stream:
    for line in file_stream:
        md5_two.update(line)
    ret = md5_two.hexdigest()
    print(ret)  # resutl = e4e372d8cbca4b48c79d5c820a517656


# 总结，以上两次针对同一个文件的不同读取加密方式，得到的结果是一致的。但后者性能的优化强很多，可以处理大文件。
