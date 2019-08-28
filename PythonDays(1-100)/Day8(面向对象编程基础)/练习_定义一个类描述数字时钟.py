class Clock(object):
	'''
		数字时钟
	'''
	def __init__(self,hour = 0,minut = 0,second = 0):
		self._hour = hour
		self._minut = minut
		self._second = second

	def run (self):
		self._second += 1
		if self._second == 60:
			self._minut += 1
			self._second = 0
			if self._minut == 60:
				self._hour += 1
				self._minut = 0
				if self._hour == 24:
					self._hour = 0

	def show_time(self):
		return '%02d:%02d:%02d'%(self._hour,self._minut,self._second)
import time

def main():
	clock = Clock(15,7,23)
	while True:
		print(clock.show_time())
		time.sleep(1)
		clock.run()
if __name__ == '__main__':
	main()
		