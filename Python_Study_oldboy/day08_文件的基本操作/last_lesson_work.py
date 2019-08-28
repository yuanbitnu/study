
def is_diffodil_number(num:int) -> bool:
	'''
		判断一个数是否是水仙花数
	'''
	if num >=100 and num <= 999:
	    a = num % 10
	    b = (num // 10) % 10
	    c = (num // 100) % 10
	    if num  == a **3 + b **3 + c **3:
	    	return True
	    else:
	    	return False	

def my_sort_list(lis:list) -> list:
	'''
		对给定列表进行排序
	'''
	for j in range(1,len(lis)):
		for i in range(0,len(lis) - 1):
			if lis[i] > lis[i+1]:
				lis[i],lis[i+1] = (lis[i+1],lis[i])
	return lis

def cai_piao() ->list:
	from random import randint
	lis = []

	for _ in range(0,7):
		random_int = randint(0,26)
		while random_int in lis:
			random_int =  randint(0,36)
		else:
			lis.append(random_int)
	return lis


print(is_diffodil_number(153))
print(my_sort_list([3,7,4,5,2]))
print(cai_piao())
