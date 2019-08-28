class Student(object):
	def __init__(self,name,age):#对象的初始化函数,创建对象时会调用
		self.name = name
		self.age = age

	def study(self,course_name):
		print('%s正在学习%s.'%(self.name,course_name))

	def watch_tv(self):
		if self.age < 18:
			print('%s未成年,只能看<熊出没>'%self.name)
		else:
			print('%s成年了,什么都可以看'%self.name)

	##卸载类中的函数,通常称之为对象的方法,这些方法就是对象可以接受的消息

def main ():
	stu = Student('张三',18)
	stu.study("编程")
	stu.watch_tv()


if __name__ =='__main__':
	main()
