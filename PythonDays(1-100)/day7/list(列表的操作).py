#一.列表的基本操作

# list1 = [1,3,5,6,70]

# print('打印列表 = ',list1,id(list1))

# list2 = list1 * 5

# print('打印列表list2: ',list2,id(list2))

# #计算列表长度(元素个数)

# print('计算列表list1长度: = ',len(list1))

# print('通过索引下标来访问list1元素: ',list1[0],list1[4],list1[-1],list1[-2])

# list1.append(100)
# print('通过append方法追加后的list1',list1) #append方法向列表最后进行追加

# list1.insert(1,200)

# print('打印通过insert方法插入后的list1',list1) # [1, 200, 3, 5, 6, 70, 100]    insert方法在指定index处插入指定值,后续值得index自动增加

# list1.remove(3)
# print('打印通过remove方法删除指定元素后的list1',list1) # [1, 200, 5, 6, 70, 100] remove方法删除指定值,如果该值不存在,则程序出现异常

# del list1[0]

# print('打印通过del删除元素后的list1',list1)

# list1.clear() #使用clear方法清空列表

# print(list1)

# 二.列表的切片操作

# names = ['孙悟空','猪八戒','沙和尚','唐僧']

# print(names,id(names))

# names += ['龙王','白骨精']

# print(names,id(names))

# fruits = ['grape','apple','strawberry','waxberry']

# for tem in fruits:
# 	print(tem.title(),end = '')
# print()

# names1 = names[1:5]

# print(names1)

# names1 = names[::-1] #通过切片步长为-1进行方向切片,获得倒转后的names1列表的拷贝

# print(names1)

# names2 = names1 # 没有复制列表,只是将names1的引用给了names2,两个变量的值中保存的引用是一样的

# print(names2,id(names2)) #names2和names1的ID是一样的

# print(names1,id(names1))

# #--------------------------------------------------------------------------

# names2 = names1[:] #通过对整个列表完整的切片来复制列表,names2指向的是names1列表的一个拷贝

# print(names2,id(names2)) #names2和names1的ID不一致

# print(names1,id(names1))

# #--------------------------------------------------------------------------

#三.列表的排序

fruits = ['orange','apple','zoo','internationlazation','blueberry']

fruits_sorted = sorted(fruits)

print(fruits,id(fruits))

print(fruits_sorted,id(fruits_sorted))

# sorted()函数返回排序后的拷贝,不会影响原列表,函数的设计就应该像sorted一样尽可能不产生副作用

#-------------------------------------------------------------------

fruits_sorted_1 = sorted(fruits,reverse = True)

print(fruits_sorted_1)

#将列表排序后进行反转
#-------------------------------------------------------------------

fruits_sorted_2 = sorted(fruits,key = len)

print(fruits_sorted_2)

