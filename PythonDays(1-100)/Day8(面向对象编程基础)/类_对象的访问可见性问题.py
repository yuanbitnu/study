class Student(object):
	def __init__(self,name,age,gander):
		self.__name = name
		self.__age = age
		self.__gander = gander
		#双下划线开头的属性属于隐藏属性,在外部无法访问

	def __study(self,course_name):#双下划线开头的方法也属于隐藏方法,在外部无法访问
		print("%s正在学习%s" %(self.__name,course_name))

def main():
	stu = Student('张三',18,'男')
	#print(stu.__name) #result = AttributeError: 'Student' object has no attribute '__name' 
	print(stu._Student__name) #result = 张三  #双下划线实现隐属性实际上是Python在进行编译时将__name改写成了_Student__name
	stu._Student__study('编程')

if __name__ == "__main__":
	main()