## 推导式，又称解析式，可以从一种数据序列构建新的数据序列的结构体，是一种语法糖，有list推导式、dict推导式、set推导式三种

##一、列表推导式
##语法：
# variable = [out_exp_res for out_exp in input_list if out_exp == 2]
# out_exp_res：                 列表生成元素表达式，可以是有返回值的函数。
# for out_exp in input_list：   迭代input_list将out_exp传入out_exp_res表达式中。
# if out_exp == 2：　　          根据条件过滤哪些值可以。

# list_comprehensions = [i**2 for i in range(0,10,2)] #out_exp_res: 带生成新列表元素的表达式的列表推导式
# print(list_comprehensions) ##result = [0, 4, 16, 36, 64]


# def fn(i):
# 	return i **2
# list_comprehensions = [fn(i) for i in range(0,10,2)] #out_exp_res: 有返回值的函数的列表推导式
# print(list_comprehensions) ##result = [0, 4, 16, 36, 64]

# list_comprehensions = [fn(i) for i in range(0,10) if i % 2 == 0] #带条件过滤的列表推导式
# print(list_comprehensions) ##result = [0, 4, 16, 36, 64]


##二、集合推导式
##语法：
# variable = {out_exp_res for out_exp in input_list if out_exp == 2}
# out_exp_res：              集合生成元素表达式，可以是有返回值的函数。
# for out_exp in input_list：迭代input_list将out_exp传入out_exp_res表达式中。
# if out_exp == 2：　　       根据条件过滤哪些值可以。

# set_comprehensions = {i **2 for i in [2,2,4,1,6]}
# 					##此处为表达式
# print(type(set_comprehensions)) #result = <class 'set'>
# print(set_comprehensions) #result = {16, 1, 4, 36}  集合的元素不重复、无序特性依旧


# def fn(i):
# 	return i**2
# set_comprehensions = {fn(i) for i in [4,6,2,2,1]}
# 					##此处为带返回值的函数
# print(set_comprehensions) ## result = {16, 1, 36, 4} 集合的元素不重复、无序特性依旧

# set_comprehensions = {fn(i) for i in range(0,10) if i % 2 == 0}

##三、字典推导式
##语法：variable = {key_exp_res:val_exp_res for out_exp in input_list if out_exp == 2}
# key_exp_res：               字典生成元素key表达式，可以是有返回值的函数。
# val_exp_res：               字典生成元素val表达式，可以是有返回值的函数。
# for out_exp in input_list： 迭代input_list将out_exp传入out_exp_res表达式中。
# if out_exp == 2：　　        根据条件过滤哪些值可以。

dic = {0:21,1:15,2:62}
dict_comprehensions = {k:v**2 for k,v in dic.items()}
					##此处为表达式
print(dict_comprehensions)



def fn(i):
	return i **2

def gn(i):
	return i **3
lis_one = [1,2,3,4]
lis_two = [3,6,9,11]

dict_comprehensions = {fn(k):gn(v) for k,v in zip(lis_one,lis_two)}
					##此处为带返回值的函数
print(dict_comprehensions)
