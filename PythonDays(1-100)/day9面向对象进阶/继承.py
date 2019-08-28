class Person(object):
	__slots__ = ('_name','_age')

	def __init__(self,name,age):
		self._name = name 
		self._age = age

	@property
	def name(self):
		return self._name
	
	@property
	def age(self):
		return self._age
	
	@name.setter
	def name(self,name):
		self._name = name

	@age.setter

	def age(self,age):
		self._age = age


	def play(self):
		print('%s正在打篮球'%self.name)

	def watch_tv(self):
		if self.age < 16:
			print("%s未成年,不能看电视"%self.name)
		else:
			print("%s成年了,可以看电视"%self.name)


class Student(Person):
	__slots__ = ('_name','_age','_grade')

	def __init__(self,name,age,grade):
		super().__init__(name,age)
		self._grade = grade

	@property
	def grade(self):
		return self._grade
	
	@grade.setter
	def grade(self,grade):
		self._grade = grade

	def study(self,course):
		print("%s的%s正在学习%s"%(self.grade,self.name,course))


class Teacher(Person):
	__slots__ = ('_name','_age','_subject')

	def __init__(self,name,age,subject):
		super().__init__(name,age)
		self._subject = subject

	@property
	def subject(self):
		return self._subject

	@subject.setter
	def subject(self,subject):
		self._subject = subject

	def teach(self):
		print('%s正在教%s'%(self.name,self.subject))
	

def main():
	stu = Student('tyb',18,'初三')
	stu.study('python编程')
	stu.watch_tv()

	tea = Teacher('张三',28,'程序设计')
	tea.teach()
	tea.watch_tv()

if __name__ == '__main__':
	main()
		