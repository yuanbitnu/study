# 一.super()方法根据当前对象,再其继承关系中从左至右寻找,对象一直不变

# class F3(object):
#     def f1(self):
#         ret = super().f1()
#         print(ret)
#         return 123


# class F2(object):
#     def f1(self):
#         print('123')


# class F1(F3, F2):
#     pass


# obj = F1()
# obj.f1()
# result = 123/None

# 二.对象方法的调用总是先调用自己类的方法,如自己类中没有则按照继承关系从左至右在其父类中寻找
# class F1(object):
#     def __init__(self, a1):
#         self.a1 = a1

#     def f2(self, arg):
#         print(self.a1, arg)


# class F2(F1):
#     def f2(self, arg):
#         print('666')


# obj_list = [F1(1), F2(2), F2(3)]
# for item in obj_list:
#     item.f2(99)

# result = 1/99   666   666
