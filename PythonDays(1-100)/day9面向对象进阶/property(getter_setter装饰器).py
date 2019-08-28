# class Person(object):

##使用getter、setter方法方式安全的访问属性
	# def __init__(self,name,age):
	# 	self._name = name
	# 	self._age = age

#定义一个getter方法访问name属性
	# def get_name(self):
	# 	return self._name

#定义一个getter方法访问age属性
	# def get_age(self):
	# 	return self._age

#定义一个setter方法设置name属性
	# def set_name(self,name):
	# 	self._name = name

#定义一个setter方法设置age属性
	# def set_age(self,age):
	# 	self._age = age

	# def play(self):
	# 	if self.get_age() <= 16:
	# 		print('%s未成年，不能玩游戏'%self.get_name())
	# 	else:
	# 		print('%s已成年，什么游戏都可以玩'%self.get_name())

# def main_one():
# 	person = Person('皮影',12)
# 	person.play()
# 	person.set_age(23)
# 	person.play()

##使用@property装饰器对getter、setter方法进行装饰，使对属性的访问既安全又方便
class Person(object):
	def __init__(self,name,age):
		self._name = name
		self._age = age

	@property
	def name(self):
		return self._name
	@name.setter
	def name(self,name):
		self._name = name

	@property
	def age(self):
		return self._age

	@age.setter
	def age(self,age):
		if age >= 0:
			self._age = age
	
	def play(self):
		if self.age < 16:
			print('%s未成年，不能玩游戏'%self.name)
		else:
			print('%s已成年 什么游戏都可以玩'%self.name)

def main_two():
	person = Person("皮影",12)

	person.play()

	person.age = 23

	person.play()






if __name__ == '__main__':
	# main_one()
	main_two()