class Course:
    def __init__(self, name, price, period):
        self._name = name
        self._price = price
        self._period = period

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price

    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, period):
        self._period = period


class Student:
    def __init__(self, name):
        self._name = name
        self._crouse_lis = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def crouse_lis(self):
        return self._crouse_li

    def select_crouse(self, crouse):
        if crouse not in self._crouse_lis:
            self._crouse_lis.append(crouse)
        else:
            print('该课程已选择,请勿再次选择')

    def show_my_crouses(self):
        print(self.crouse_lis)

    def del_crouse(self, crouse):
        self.crouse_lis.remove(crouse)


def run():
    fun_list = []
    print('''主程序
    1.根据Crouse类创建10个课程
    2.用户输入学生名字,动态创建学生对象
    3.查看所有课程
    4.为学生选课
    5.删除已选课程
        ''')
    user_choice = input('请选择需要执行的功能序号:')


run()

# crouse = Course('张三', 12, '无语')
# print(crouse.name, crouse.price, crouse.period)
# crouse.name = '李四'
# crouse.price = 36
# crouse.period = '简体'
# print(crouse.name, crouse.price, crouse.period)
