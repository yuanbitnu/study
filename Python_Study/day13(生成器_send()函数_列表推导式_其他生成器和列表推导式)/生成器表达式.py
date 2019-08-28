##生成器表达式，即使用一个类似于生成式的语法格式创建一个生成器，创建好的生成器和使用生成器函数创建的生成器一样可以使用__next__()或者send()方法调用取值
##语法：（结果 for循环 条件） ##生成器的创建是使用一对“()”
generator = (i**2 for i in range(10) if i % 2 == 0)
print(generator)
print(generator.__next__())
print(generator.send('str')) ##使用生成器表达式创建的生成器在使用send(arg)方法取值时，传入的arg参数值等同于无效，因为没有任何方式可以拿到它