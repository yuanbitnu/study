class Class():
	pass

c = Class()

print(c) #<__main__.Class object at 0x0000024770D43080>

print(type(Class)) #<class 'type'>

My_Class = type('Class_type',(),{'a':1,'b':2})

my_class = My_Class()

print(my_class)