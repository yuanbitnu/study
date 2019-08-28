def nums(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
	 return nums(n-1) + nums(n)




def pri(n):
	for i in range(1,n+1):
		print(' '*(n-i),end = '')
		for j in range(1,i+1):
			print(nums(j)," ")
			

pri(7)