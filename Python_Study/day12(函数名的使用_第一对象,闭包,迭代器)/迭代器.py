##一、可迭代对象（iterable）,(list,tuple,set,dict等都是可迭代对象)，可以使用for while 进行循环遍历
##二、迭代器，(iterator),可迭代对象中一定会有一个迭代器，迭代器中一定会有一个迭代器和一个__next__()方法
##三、dir()方法，使用dir()方法可以查看一个对象具有哪些方法
##四、迭代器针对不同的数据类型会有不同的实现，但统称为迭代器

##迭代器的特点：
#一、迭代器只能向前
#二、迭代器的惰性机制（只能调用了__next__()方法才能获取值，调用一次获取一个，不会自动取获取，必须调用__next__()方法）
#三、节省内存



##print(dir(list))

'''
	result = ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', 
	'__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
	 '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__','__init_subclass__',

	 '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__'，

##(list对象中具有一个__iter__()方法，该方法用于获取迭代器)

	   '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', 
	   '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend',
	    'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
'''

lis = [1,2,3,4,5]
iterator = lis.__iter__()  ##获取lis对象中的迭代器
print(dir(iterator)) ##查看迭代器中具有哪些方法

'''
	result = ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__',
	 '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', 
	 '__iter__', '__le__', '__length_hint__', '__lt__', '__ne__', '__new__', 
##(lis对象的迭代器对象中也有一个__iter__()方法，该方法用来返回迭代器本身)
	 '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__',
##(lis对象的迭代器对象中有一个__next__()方法，该方法用来获取lis对象中的元素，每调用一次获取一个元素)
	  '__sizeof__', '__str__', '__subclasshook__']
'''



##for循环内部就是迭代器：
lst = [1,2,3,1]
iterator = lst.__iter__() ##获取lst(列表对象)中的迭代器
while True:
	try:
		item = iterator.__next__()  ##调用迭代器中的__next__()方法获取元素
		print(item)
	except StopIteration : ##当迭代器将列表中的元素获取完毕后继续调用__next__()方法时会抛出StopIteration异常
		break






