def fei (n):
	a,b = 0,1
	if n < 0:
		return None
	elif n == 0:
		return a
	elif n == 1:
		return b
	else:
		return fei(n-1) + fei(n-2)

print(fei(9))


def fib(n):
	a,b = 0,1
	for _ in range(n): # range()函数如果只写一个参数n,则表示range()的元素范围是0到n-1(包前不包后),如果n=0,则没有任何元素
		a, b = b, a + b
		yield a

generator = fib(9)

for n in generator:
	print(n)
