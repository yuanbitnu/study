## 函数名实际上也是变量名,变量名怎么用函数名也可以怎么用

##函数名就是变量名,可以给函数名再赋其他类型的值
# def fn(a,b):
# 	print(a+b)
# fn(1,2) ## result = 3

# fn = 1
# # fn(1,2) ## TypeError
# print(fn) ## result = 1


## 可以和变量之间相互赋值
# def fn(a,b):
# 	print(a+b)
# num = 10
# print(num) ##result = 10
# fn(1,2) ##result = 3

# num = fn ##将函数名赋值给变量名
# num(1,2) ##result = 3

# num_two = 20
# fn = num_two ##将变量赋值给函数
# print(fn) ## result = 20


## 函数名可以作为容器(list\tuple\set\dict)的元素
# def fn_1():
# 	print('我是fn_1函数')
# def fn_2():
# 	print('我是fn_2函数')
# def fn_3():
# 	print('我是fn_3函数')

# lis = [fn_1,fn_2,fn_3]
# for function in lis: ## resutl = 我是fn_1函数 我是fn_2函数 我是fn_3函数
# 	function()


##函数名可以作为函数的返回值进行返回
# def outter():
# 	a = 10
# 	def inner():
# 		print(a)
# 		print('我是inner()函数')
# 	return inner
# function = outter()
# function()  # result 打印：10 我是inner()函数

##函数名可以作为参数传递给函数
# def add(a,b):
# 	print(a+b)

# def fn(function,a,b):
# 	function(a,b)

# fn(add,2,3) ##将add函数作为参数传递给fn函数  result = 5








