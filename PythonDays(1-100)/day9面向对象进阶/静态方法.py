##静态方法一般用作工具类的方法,和对象无关,相当于将一些工具方法放在一个类里面方便调用
from math import sqrt
class Triangle(object):
	__slots__ = ('_a','_b','_c')

	def __init__(self,a,b,c):
		self._a = a
		self._b = b 
		self._c = c

	@property
	def a(self):
		return self._a

	@property
	def b(self):
		return self._b

	@property
	def c(self):
		return self._c

	@a.setter
	def a(self,a):
		self._a = a

	@b.setter
	def b(self,b):
		self._b = b

	@c.setter
	def c(self,c):
		self._c = c

	#判断给定的三条边是否能组成三角形
	@staticmethod #将一个方法装饰为一个静态方法
	def is_valid(a,b,c):#此时还不确定三条边能不能构成三角形,因此还没有三角形对象,属于这个方法是不属于三角形对象的方法,
						#因此可以使用静态方法来解决这类问题
		return a + b > c and a + c > b and b + c > a

	#计算周长
	def perimeter(self):
		return self.a + self.b + self.c

	#计算面积
	def area(self):
		p = self.perimeter()/2
		return sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))


def main():
	a,b,c = 3,4,5
	if Triangle.is_valid(a,b,c):
		traingle = Triangle(a,b,c)
		perimeter =	traingle.perimeter() 
		area = traingle.area()
		print(perimeter)
		print(area)
	
if __name__ == '__main__':
	main()
	