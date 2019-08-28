##生成器的本质就是手写的迭代器.
##特点和迭代器一样
##取值方式和迭代器一样也是通过__next__()
##创建方式:1、生成器函数；2、生成器表达式

##一、yield 关键字,功能和return关键字一样,将需要返回的内容返回
# def fn():  ##使用yield关键字返回内容的函数即为生成器函数
# 	yield 'yield关键字返回的内容'
# 	print('yield关键字后的函数体内容')
# 	yield '第二个yield关键返回的内容'
# generator = fn() ##调用fn()生成器函数,此时不会执行函数体中的内容,而是返回一个'生成器',此时的generator即为一个生成器
# print(generator) ## result = <generator object fn at 0x00000212AAA5BA20>
# print(generator.__next__()) ## result = 'yield关键字返回的内容'  调用生成器的__next__()方法执行生成器中的函数体,并且在遇到yield后即返回内容,函数体暂停,直到再次调用__next__()方法,函数继续执行到下一个yield关键字之后的内容
# print(generator.__next__()) ## result = yield关键字后的函数体内容 第二个yield关键返回的内容


##二、生成器函数,调用生成器函数，产生一个生成器，函数体中带有yield关键字的函数就是生成器函数
# def fn():
# 	for i in range(0,5):
# 		yield i  ## 该fn函数就是一个生成器函数

# generator = fn() ##调用生成器函数，仅仅产生一个gennerator生成器,不会执行函数体中的内容
# print(generator)  ##result = <generator object fn at 0x000002122F2EBA20> 

# print(generator.__next__()) ##生成器的本质就是迭代器，通过调用__next__()方法，一个一个的从生成器中获取值
# print(generator.__next__())
# print(generator.__next__())
# print(generator.__next__())
# print(generator.__next__())
# print(generator.__next__()) ##当生成器中的yield语句都执行完后继续调用__next__()方法则会引发和迭代器一样的 StopIteration异常

##三、生成器的__next__()方法和send()方法
#__next__()方法，调用一次则从生成器中取一个值
#send(arg)方法，具有和__next__(arg)方法一样的功能，同时会将其arg参数的值传递给上一个yield的位置，例如：
def fn():
	print('one_time yield before str')
	one_time = yield 'one yield key_word return'
	print(one_time)
	print('two_time yield before str')
	two_time = yield 'two yield key_word return'
	print(two_time)
	print('three_time yield before str')
	three_time = yield 'three yield key_word return'
	print(three_time)

generator = fn()
#print(generator.send('一')) #result = TypeError: can't send non-None value to a just-started generator  第一个yield不能使用send()方法，因为没有上一个yield
print(generator.__next__())  #result = one_time yield before str  one yield key_word return
print(generator.send('send arg 参数 one'))
print(generator.send('send arg 参数 two'))
#print(generator.__next__()) ##最后一个yield使用__next__()方法不能为倒数第二个yield位置赋值，并且会抛出StopIteration异常，
#print(generator.send('send arg 参数 three')) ##最后一个yield使用send()方法，没有意义，拿不到传入send的值，因为执行到了yield之后继续调用生成器则会抛出StopIteration异常



