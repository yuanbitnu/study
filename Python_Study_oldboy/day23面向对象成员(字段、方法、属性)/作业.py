# 1、面向对象的三大特性：封装、继承、多态
# 2、面向对象的变量(字段)分为哪几种：
#   类变量(字段)
#   实例变量(字段)
# 3、面向对象中的方法有哪几种：
#   实例方法 定义无装饰器修饰的在类中的方法（需要自带参数self）
#   类方法(使用@classmethod装饰器修饰，需自带参数cls)
#   静态方法(使用@staticmetho装饰器修饰，可以不需要任何参数)
# 4、面向对象中的属性有什么：
#   属性 使用@property装饰器修饰的实例方法，使用属性可以在调用时不带()
# 5、简述静态方法和类方法的区别
#   定义的区别：类方法使用@classmethod 修饰，而且需要传入一个必须的类参数cls
#              静态方法使用@staticmethod 修饰，不需要传入必须的参数
#   调用上的区别： 类方法调用时，当前类会被自动传入类方法
#                 静态方法调用时，不会自动传递任何参数
# 6、面向对象公有和私有成员，在编写和调用时有哪些不同？
#   编写时：公有成员可以是任何符合变量命名规范的名称
#           私有成员必须在变量名前面加上‘__’
#   调用时：公有成员在类的内部和外部都能被调用
#          私有成员只能在类的内部被调用
#   原理：python中的公有和私有本质上只是python编译器在编译时将变量名__age 编译成了 _Cls__age


# 7、看代码，写结果
# class Foo(object):
#     a1 = 11
#     a2 = 12

#     def __init__(self):
#         self.a1 = 1
#         self.a3 = 3


# obj = Foo()

# print(obj.a1)  # result = 1
# print(obj.a2)  # result = 12

# # print(Foo.a3)  # 报错,因为类字段中没有a3
# print(Foo.a1)  # result = 11


# 总结:
#   1、使用类调用字段时，只会在找类字段
#   2、使用对象调用字段时，会先在实例字段中寻找，如果没有则会去类字段中寻找


# 8、

# class Foo_one(object):
#     a1 = 1
#     __a2 = 2

#     def __init__(self, num):
#         self.num = num
#         self.__salary = 1000

#     def get_data(self):
#         print(self.num + self.a1)


# obj_one = Foo_one(669)

# print(obj_one.num)  # result = 669
# print(obj_one.a1)  # result = 1  此时实例字段中没有a1，python会去类字段中找
# # print(obj_one.__salary)  # 报错AttributeError，带__的实例字段属于私有字段，在类的外部无法访问

# # print(obj_one.__a2) # 报错AttributeError,此时会先在对象字段中找__a2,找不到再去类字段中找，类字段中有__a2,但是带__的类字段属于私有字段，在类的外部无法访问
# print(Foo_one.a1)  # result = 1 此时通过类访问类字段
# # print(Foo_one.__a2)  # 报错AttributeError,此时会先在对象字段中找__a2,找不到再去类字段中找，类字段中有__a2,但是带__的类字段属于私有字段，在类的外部无法访问，通过类访问类字段是可行的，但是带__的类字段属于私有字段，在类的外部无法访问


# 9、

# class Foo_two(object):
#     num = 111

#     def __init__(self, name):
#         self.name = name
#     # 类方法可以使用类来调用，也可以使用实例对象来调用，会将该类或该实例对象对应的类绑定到类方法的第一个参数上面

#     @classmethod
#     def fun(cls):
#         print(cls, cls.num)


# Foo_two.fun()  # 通过类调用类方法，会将当前类绑定到类方法的第一个参数上

# obj_two = Foo_two('zhang')  # 通过实例对象调用类方法时也会将该实例对应的类绑定到类方法的第一个参数上
# obj_two.fun()


# 10
class Foo_three:

    @classmethod
    def fun(cls):
        print(cls)

    def fun1(self):
        self.fun()
        Foo_three.fun()


obj = Foo_three()
obj.fun1()

'''
    result:
    <class '__main__.Foo_three'>
    <class '__main__.Foo_three'>
'''