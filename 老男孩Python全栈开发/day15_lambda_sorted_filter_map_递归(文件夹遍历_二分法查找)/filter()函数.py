# filter()用来过滤可迭代对象中的元素
lis = ['张三', '李四', '张铁林', '王五']
lis_new = filter(lambda item: item[0] != '张', lis)  # 过滤掉姓张的元素
print(lis_new)  # result = <filter object at 0x00000173F2283160>
print('__iter__' in dir(lis_new))  # result  True  判断lis_new对象是不是可迭代对象
print(list(lis_new))  # result = ['李四', '王五']


filter()##函数中的function参数是一个将传入对象进行运算, 返回True的留下, 返回False的过滤掉
