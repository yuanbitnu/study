##和静态方法类似,python可以在类中定义类方法,类方法和对象方法一样会自动传递一个参数,约定为cls
	#cls表示和当前类相关的信息的对象(类本身也是一个对象,属于Type类)

from time import time,localtime,sleep
class Clock(object):

	__solts__ = ("hour",'minute','second') #限定了对象初始化时可以绑定的属性

	def __init__(self,hour = 0,minute = 0,second = 0):
		self._hour = hour 
		self._minute = minute
		self._second = second

	@property
	def hour(self):
		return self._hour
	@property
	def minute(self):
		return self._minute
	@property
	def second(self):
		return self._second
	
	@hour.setter
	def hour (self,hour):
		self._hour = hour

	@minute.setter
	def minute (self,minute):
		self._minute = minute

	@second.setter
	def second(self,second):
		self._second = second

	def run(self):
		self.second +=1
		if self.second == 60:
			self.minute +=1
			self.second = 0
			if self.minute == 60:
				self.hour +=1
				self.minute = 0
				if self.hour == 24:
					self.hour = 0
	#类方法
	@classmethod
	def now (cls):
		now_time = localtime(time())
		return cls(now_time.tm_hour,now_time.tm_min,now_time.tm_sec)#使用cls创建Clock对象,并返回

	def show_time(self):
		print('%2d:%2d:%2d'%(self.hour,self.minute,self.second))

def main():
	clock = Clock.now()
	while True:
		clock.show_time()
		clock.run()
		sleep(1)


if __name__ == '__main__':
	main()


