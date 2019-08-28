##闭包--即是一个函数嵌套，内部inner()函数调用了外部outter()函数内的局部变量，并将内部函数返回

##示例：
def outter():
	a = 10
	def inner():
		print(a) ##调用了外部outter()函数的局部变量
	return inner
##闭包的优点
#一是保证了外部变量不受侵害（随意更改）
#二是使得外部函数的变量可以常驻内存，方便以后的调用(这种特性的原因是为了保证内部函数随时可以调用,必须保证外部函数的变量一直在内存)

outter()() ##先执行outter(),此时得到inner,再执行inner(),等同于如下代码:

inner = outter() ##这种方式的调用,将内部inner函数返回出来,方便随时调用,此时为了保证inner函数能够随时被调用,outter函数的变量a则必须一致存在于内存中
inner()

##判断一个函数是否是闭包,使用__closure__
print(outter.__closure__) ## result = None 表示不是闭包
print(inner.__closure__) ## result = (<cell at 0x0000025AB0E13828: int object at 0x00007FF8F9FF63B0>,)  表示是闭包

print(inner.__closure__[0].cell_contents) ##result = 10  按照索引的方式返回闭包的值