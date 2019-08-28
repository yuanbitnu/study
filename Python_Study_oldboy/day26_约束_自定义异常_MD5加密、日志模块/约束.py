# 一、 通过定义一个父类，让其他需要被约束的类继承自该父类并实现该父类中的方法，以达到约束的效果----常用


class Base_class():
    def send(self, message):
        raise NotImplementedError  # 通过抛出异常的方式约束继承该类的子类必须实现该方法


class Sub_one_class(Base_class):  # 按照父类的约束，重写了父类中的send方法。
    def send(self, message):
        print(message)


class Sub_two_class(Base_class):  # 未重写父类的方法
    def fun(self, message):
        pass


# Sub_one_class 对象调用send方法时只会调用自己类中重写父类的send方法
sun_one_obj = Sub_one_class()
sun_one_obj.send('message')


# Sub_two_class 对象调用send方法时因为该类未重写父类send方法，因此python解释器会执行父类中的send方法，最终抛出NotImplementedError 异常
sub_two_class = Sub_two_class()
# sub_two_class.send('message')
#  二、通过抽象类和抽象方法对类中方法进行约束---不常用

from abc import ABCMeta, abstractmethod  #  定义抽象类必须导入


class Base(metaclass=ABCMeta):  # 定义一个抽象类
    def fun(self):
        print(123)

    @abstractmethod  # 使用abstractmethod装饰器定义一个抽象方法
    def send(self, message):
        print(message)  # 抽象方法的方法体中可以有具体的实现代码，也可以没有实现代码


class Sub_class_one(Base):  # 严格按照抽象类中的方法重写了父类中的抽象方法
    def send(self, message):
        print(message)


class Sub_class_two(Base):  # 未严格按照父类重写抽象方法，少了一个参数
    def send(self):
        print('未严格按照父类重写抽象方法，少了一个参数')


class Sub_class_three(Base):  # 未重写父类中的抽象方法
    def fun(self):
        print('Sub_class_three类中的 fun 方法')


sub_class_one = Sub_class_one()
sub_class_one.send('666')  # result = 666


sub_class_two = Sub_class_two()
sub_class_two.send()  # result = 未严格按照父类重写抽象方法，少了一个参数


# result = Can't instantiate abstract class Sub_class_three with abstract methods send  (构建对象时就会抛出异常，表示未实现父类中的抽象方法send)
sub_class_three = Sub_class_three()


'''
    总结：
    一、python中对类中方法的约束(类中必须有某个方法)可以通过两种方式实现：
        1.（常用）通过自定义一个父类，在需要约束的方法中主动抛出“NotImplementedError”异常，强制其子类重写父类中需要约束的方法
        2.（不常用）通过抽象类和抽象方法进行约束

    二、python中的约束只能约束子类必须实现该方法，对该方法的参数无法进行约束

    三、约束的应用场景
        多个类的内部都必须有某些方法时，需要使用  基类+异常NotImplementedError进行约束

'''
