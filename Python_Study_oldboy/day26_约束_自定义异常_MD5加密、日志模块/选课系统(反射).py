# crose_list = []

# fun_list = [
#     ['选课', 'select_crouse'],
#     ['查看已选课程', 'show_crouse'],
#     ['删除课程', 'del_crouse']
# ]


class Crouse():
    """docstring for Crouse"""
    crose_list = []

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
    """docstring for Student"""
    fun_list = [
        ['选课', 'select_crouse'],
        ['查看已选课程', 'show_crouse'],
        ['删除课程', 'del_crouse']
    ]

    def __init__(self, name):
        self._name = name
        self._crouse = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def select_crouse(self):
        for key, item in enumerate(Crouse.crose_list, 0):
            print(key, '.', item.name)
        user_choice = int(input('请选择课程：'))
        crouse = Crouse.crose_list[user_choice]
        if crouse not in self._crouse:
            self._crouse.append(crouse)
        else:
            print('该课程已选择，请不要重复选择')

    def show_crouse(self):
        # print(self._crouse)
        choice_crouse = self._crouse
        print('已选课程如下：')
        for key, item in enumerate(choice_crouse, 0):
            print(key, '.', item.name)

    def del_crouse(self):
        choice_crouse = self._crouse
        print('已选课程如下：')
        for key, item in enumerate(choice_crouse, 0):
            print(key, '.', item.name)
        del_index = int(input('请输入需要删除的课程：'))
        choice_crouse.remove(choice_crouse[del_index])
        self._crouse = choice_crouse
        print('已选课程如下：')
        for key, item in enumerate(choice_crouse, 0):
            print(key, '.', item.name)


def run():
    for i in range(1, 11):
        Crouse.crose_list.append(Crouse('课程%s' % i, 90, 90))
    stu_name = input('请输入学生姓名：')
    student = Student(stu_name)
    while True:
        print('*' * 15, '功能菜单', '*' * 15)
        for k, item in enumerate(Student.fun_list, 1):
            print(k, '.', item[0])
        print('*' * 34)
        choice_num = int(input('请输入想要执行的选项：'))
        index = choice_num - 1
        fun_name = Student.fun_list[index][1]
        fun = getattr(student, fun_name)
        fun()


    # print('''1.选课
    # 2.查看已选课程
    # 3.删除已选课程
    #     ''')
run()
