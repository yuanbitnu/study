##使用可变参数列表,接收n个数字并求和
# def add(*nums):
# 	result = 0
# 	for num in nums:
# 		result += num
# 	return result
# print(add(1,2,3,4,5,6,7,8,9))

##阅读下列代码,写出a,b,c的值
# a = 0
# b =20
# def test5(a,b):
# 	print(a,b) ##result 20,0
# c = test5(b,a)  ##函数test5没有返回任何值,因此c = None
# print(c) ##result None

##使用可变参数列表,传入多个可迭代对象(字符串,列表,元祖,集合等)将每个实参的每个元素依次添加到函数的可变参数中
##例如传入函数的参数为([1,2,3],(22,34)),最终的args为(1,2,3,22,34)
# def fn(*args):
# 	print(args)

# fn(*[1,3,5],*(22,3,1),*{6,3,7}) ##将每个元素都解包后传入fn函数

##定义一个接收两个数字参数的函数值返回
# def fn(a,b):
# 	return a if a < b else b
# print(fn(5,3))

##定义一个接收可迭代参数的函数,将可迭代对象的每个元素以"_"相连,形成新的字符串并返回
# def fn(iterable):
# 	lis = []
# 	for item in iterable:
# 		lis.append(str(item))
# 	return '_'.join(lis)

# print(fn({1,2,3,4,5}))

##定义一个接收n个数的函数,返回字典{'max':最大值,'min':最小值}
# def fn(*nums):
# 	_max = max(nums)
# 	_min = min(nums)
# 	return {'max':_max,'min':_min}

# print(fn(3,4,2,5,6))

##定义一个函数,传入一个int型参数n,求n的阶乘
# def factorial(n):
# 	if n ==1:
# 		return 1
# 	else:
# 		return n * factorial(n-1)
# print(factorial(4))

##定义一个函数,返回扑克牌列表,52项,每项一个元组
# def fn():
# 	result_lis = []
# 	huase = ['红心','黑桃','方片','草花']
# 	dianshu = [2,3,4,5,6,7,8,9,10,'A','J','Q',"k"]
# 	for color in huase:
# 		for i in dianshu:
# 			result_lis.append((color,i))
# 	print(result_lis)
# fn()