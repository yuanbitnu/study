## map函数会根据提供的函数对指定的序列进行映射(对序列中的所有元素进行相应的处理,返回一个新的序列)
lis = [1,2,3,4,5,6]

def fn(item):
	return item **2

lis_new = map(fn,lis)
lis_new_two = map(lambda item:item **2,lis)

if '__iter__' in dir(lis_new):
	print(list(lis_new))
	print(list(lis_new_two))
##以上这种应用方式和列表推导式基本一致
lis_new_three = [item **2 for item in lis]
print(lis_new_three)

##map()函数常见的应用方式是对数据对阶段的操作,fn1第一阶段,fn2第二阶段,fn3第三阶段
 map(fn3,map(fn2,map(fn1,lis)))