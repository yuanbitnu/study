class Person(object):
	#限定当前类的对象只能绑定_name和_age属性
	#__slots__ = ('_name','_age') # result = 抛出异常AttributeError: 'Person' object has no attribute '_gander' ；__slots__只限定当前类的对象，不会限制子类

	#限定当前类的对象只能绑定_name和_age和_gander属性
	__slots__ = ('_name','_age','_gander')

	def __init__(self,name,age,gander): #绑定了_name _age _gander 属性
		self._name = name
		self._age = age
		self._gander = gander

	@property
	def name(self):
		return self._name

	@property
	def age(self):
		return self._age

	@property
	def gander(self):
		return self._gander

	@name.setter
	def name(slef,name):
		self._name = name

	@age.setter
	def age(self,age):
		if age >= 0:
			self._age = age

	@gander.setter

	def gander(self,gander):
		self._gander = gander


	def play(self):
		if self._age >= 16:
			print('%s已成年，可以玩任何游戏'%self._name)
		else:
			print('%s未成年，不能玩游戏'%self._name)
	

def main():
	person = Person('皮影',12,'男')
	person.play()



if __name__ == '__main__':
	main()