# random 随机数模块
# 1.取随机小数;2.取随机整数;3.从squence或set中取随机个元素;4.打乱squence中的元素(set中的元素本就是无序的)
import random
# random模块的方法

# # 1.random.random() 取随机小数值,取值范围[0,1)
# print(random.random())

# # 2.random.uniform(a,b) 取随机小数值,取值范围[a,b)
# print(random.uniform(2, 3))

# # 3.random.random.randomint(a,b) 取随机整数值,取值范围[1,2],包前包后
# print(random.randint(1, 2))

# # 4.random.randrange(a,b) 取随机整数值,random和range(a,b)的结合体,取值范围[a,b),包前不包后
# print(random.randrange(1, 5))

# 5.random.choice(list) 从squence或set 中随机取一个元素返回

# lis = [31, 42, 3, 11, 21, 9]
# print(random.choice(lis))

# 6.random.sample(list,k) 从squence或set中随机取 K 个unique(唯一)的元素组成一个新的list(列表)返回

# lis = [31, 42, 3, 11, 21, 9]
# print(random.sample(lis, 2))

# 7.random.shuffle(lis) 在原squence基础上随机打乱元素的位置
# lis = [31, 42, 3, 11, 21, 9]
# random.shuffle(lis)
# print(lis)
