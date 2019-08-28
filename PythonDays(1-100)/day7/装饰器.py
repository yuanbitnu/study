def say_hello():
	print('Hello World')

def add(a,b):
	result = a+b
	print(result)
	return result

def my_sort(a):
	new =  sorted(a,key = int)
	return new

def begin_end(fn):  #定义一个装饰器函数,用来返回装饰好了的函数

	def new_say_hello(*args,**kargs): #定义一个由装饰器返回的函数

		print('begin......')
		result = fn(*args,**kargs)
		print('end......')
		return result
	return new_say_hello

##原理用法

new_say_hello  = begin_end(say_hello) #使用begin_end装饰器来装饰say_hello函数,返回经过装饰后的函数

new_say_hello()  #调用经过装饰后的函数


new_add = begin_end(add)
new_add(123,456)


new_my_sort = begin_end(my_sort)
print(new_my_sort(['12',1,3,'2',42,'23'])) 


##python用法,在定义某个函数时使用@+装饰器函数 对定义的函数直接进行装饰,调用时则可以通过调用定义的函数名来实现装饰后的效果,但mul函数未经过装饰的功能则不再能够调用实现

@begin_end
def mul(a,b):
	result = a*b
	print(result)
	return result

mul(2,3)