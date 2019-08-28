import sys

def main():
	## 元组的操作
	
	#定义一个空元祖
	t = () 
	print(type(t)) # result = <class 'tuple'>

	#定义一个非空元祖
		#定义一个只有一个元素的元祖
	t = ('a')
	print(type(t)) #result = <class 'str'> 
	t1 = (1)
	print(type(t1)) #<class 'int'>
	print(t) #result = a
		#注意:在定义只有一个元素的元祖时如果只写一个值,则编译器会将其识别为单个类型
		#因此在创建单个元素的元祖时需要在单个元素后面加上"逗号",如下:
	t = ('a',) #在单个元素后面加逗号
	print(type(t)) #result = <class 'tuple'> 
	print(t) #result = ('a',)
		#定义一个具有多个元素的元祖
	t = ('体育部',38,True) # result = ('体育部', 38, True)
	print(t)

	#获取元祖中的元素
	print(t[0]) #通过索引获取元素中的元素
	print(t[2])

	for n in t: #遍历元祖中的元素
		print(n)

	#t[0] = '数学部' # result = TypeError(抛出异常,因为tuple属于不可变序列,不能给元祖中的元素重新赋值,而list可以) 

	#将元祖转换成列表
	t_list = list(t)
	print(t_list) #result = ['体育部', 38, True]
	print(id(t)) #result = 1253259130344
	print(id(t_list)) #result = 1253259762312
		#使用list()将一个元祖转换成列表时是根据元祖元素重新创建了一个新列表返回
	
	tup = (1,2,3,'张三','李四','王五','赵倩')
	print(sys.getsizeof(tup)) #result = 104

	lis = [1,2,3,'张三','李四','王五','赵倩']
	print(sys.getsizeof(lis)) #result = 120

		#创建完全一样的元素,使用tuple(元祖)占用的内存以及花费时间都要元小于使用list(列表)


	



if __name__ =='__main__':
	main()