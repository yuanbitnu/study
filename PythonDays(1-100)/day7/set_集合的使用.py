##python中的集合和数学中的集合一样,不允许有重复元素,而且可以进行交集、并集、差集等运算

	##不论以何种方式创建的集合,集合中元素的存储是无序的,每次编译元素的排序都不一定相同
def main():
	#创建空集合
	
	s = {} #不能使用{}方式创建空集合，编译器会将其识别为dic（字典）
	print(len(s))
	print(type(s)) # resule = <class 'dict'> 

	s = set() #使用set()方法创建空集合
	print(s)# result = set()
	print(len(s))
	print(type(s)) # result = <class 'set'>

	s = {1,2,6,3,4,4,4,2,5} #使用{}创建非空集合
	print(s) #set会去掉重复元素,并且元素在set中是无序的
	#注意:
	#s = set(1,2,3) # result = TypeError: set expected at most 1 arguments, got 3 抛出异常;不能使用该方法传递元素创建非空集合
	
	lis = ['张三','张三','王五',1,1,3]
	lis_set = set(lis) 
	print(lis_set) # result = {'王五', 1, 3, '张三'}  去掉了list中的重复元素,且元素排列无序 
	print(type(lis_set)) #result = <class 'set'>

	tup = ('张三','张三','王五',1,1,3)
	tup_set = set(tup)
	print(tup_set) # result = {'张三', '王五', 3, 1} 去掉了tuple中的重复元素,且元素排列无序
	print(type(tup_set))
	#注意:
	#可以使用set()函数将列表,元祖转为set,但是会去掉重复元素,且元素排列无序
	
	#使用set内置方法
	
		#set.add()方法向集合中添加一个元素,且无序的
	s = {1,2,3,3,3,2}
	print('add前的set = ',s) # result = {1, 2, 3}
	s.add(5)
	s.add(0)
	s.add('张三')
	print('add后的set = ',s) # result = {0, 1, 2, 3, 5, '张三'}

		#set.update()方法将一个集合、列表、元组合并到该集合中，去掉重复元素且排列是无序的
	s = {'张三','李四','王五',1,2,2,5}
	lis = ['张三','李四','王麻子',100,1,27,5]
	tup = ('张三','李四','王麻子',100,1,27,5)
	se = {'张三','李四','王麻子',100,1,27,5}
	print('update前的set = ',s)
	s.update(se)
	print('update后的set = ',s)
		
		#set.remove()和set.discard()方法,功能都是删除指定元素,区别在删除不存在的元素时remove会抛异常,而discard则不会抛出异常
	s = {'张三','李四','王五',1,2,2,5}
	print('remove和discard前的set = ',s)
	s.remove("张三")
	# s.remove('王麻子') # result = KeyError: '王麻子',使用set.remove()方法删除不存在的元素时会抛出异常
	s.discard('李四') # result = 更改后的set =  {2, 1, 5, '王五'} 
	s.discard('王麻子') # 使用set.discard()方法删除元素时如果元素不存在也不会报错
	print('remove和discard后的set = ',s)

		#set.pop()方法,从集合中随机移除一个元素,并将此元素返回
	s = {'张三','李四','王五',1,2,2,5}
	print('pop前的set = ',s)
	result =  s.pop()
	print('pop出去的元素',result)
	print('pop后的set = ',s)

		#set.clear()方法从集合中移除所有元素,无返回值
	result = s.clear()
	print(result) # result = None
	print(s) # result = set()

	#set(集合)的交集、并集、差集、对称差运算

		#交集：两个集合共有的元素
			#使用&符号求交集
	s1 = {1,2,3,6,7,8,9}
	s2 = {2,3,45,6,78}
	result = s1 & s2  #result = {2, 3, 6}
	print(result)
			#使用set.intersection()方法求交集
	s1 = {1,2,3,6,7,8,9}
	s2 = {2,3,45,6,78}
	result = s1.intersection(s2) #result = {2, 3, 6}
	print(result)	

		#并集:把两个集合的所有元素合并在一起组成的集合(没有重复的元素)
			#使用|符号求并集
	s1 = {1,2,3,6,7,8,9}
	s2 = {2,3,45,6,78}
	result = s1 | s2 #result = {1, 2, 3, 6, 7, 8, 9, 45, 78}
	print(result)
			#使用set.union()方法求并集
	s1 = {1,2,3,6,7,8,9}
	s2 = {2,3,45,6,78}
	result = s1.union(s2) #result = {1, 2, 3, 6, 7, 8, 9, 45, 78}
	print(result)

		#差集:A和B的差集，即将A中去掉和B的交集部分
			#使用"-"号求差集
	s1 = {1,2,3,6,7,8,9}
	s2 = {2,3,45,6,78}
	result = s1 - s2 #result = {8, 1, 9, 7}
	print(result)
	result = s2 - s1 #result = {45, 78}
	print(result)
			#使用set.difference()方法求差集
	s1 = {1,2,3,6,7,8,9}
	s2 = {2,3,45,6,78}
	result = s1.difference(s2) #result = {8, 1, 9, 7}
	print(result)
	result = s2.difference(s1) #result = {45, 78}
	print(result)

		#对称差运算：去掉A和B的交集部分后，A和B剩下的元素组成的集合
			#使用'^'符号求对称差运算
	s1 = {1,2,3,6,7,8,9}
	s2 = {2,3,45,6,78}
	result = s1 ^ s2 #result = {1, 7, 8, 9, 45, 78}
	print(result)
	result = s2 ^ s1 #result = {1, 7, 8, 9, 45, 78}
	print(result)
			#使用set.symmetric_difference()方法求对称差运算
	s1 = {1,2,3,6,7,8,9}
	s2 = {2,3,45,6,78}
	result = s1.symmetric_difference(s2)  #result = {1, 7, 8, 9, 45, 78}
	print(result)
	result = s2.symmetric_difference(s1) #result = {1, 7, 8, 9, 45, 78}
	print(result)

	##set(集合)的超集、子集的判断
		#超集的判断：A中元素包括了B中的所有元素，则A是B的超集，B是A的子集
			#使用>=号来判断是否为超集
	s1 = {1,2,3,6,7,8,9}
	s2 = {2,3,6}
	print(s1 >= s2) #result = True
	print(s1 <= s2) #result = False
			#s使用set.issuperset()方法判断A集合是否是B集合的超集
	s1 = {1,2,3,6,7,8,9}
	s2 = {2,3,6}
	print(s1.issuperset(s2)) #result = True
		#子集的判断：A中的元素再B中全都有，则A是B的子集
			#使用<=判断是否为子集
	s1 = {1,2,3,6,7,8,9}
	s2 = {2,3,6}
	print(s2 <= s1) #result = True
	print(s2 >= s1) #result = False
			#s使用set.issubset()方法判断A集合是否是B集合的超集
	s1 = {1,2,3,6,7,8,9}
	s2 = {2,3,6}
	print(s2.issubset(s1)) #result = True



if __name__ == '__main__':
	main()