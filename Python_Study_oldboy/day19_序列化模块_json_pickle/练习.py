import os
import pickle
import random
import math
import re
# 1.定义一个函数，接受一个路径参数，如果该路径是一个文件，则执行这个文件，如果该路径是一个文件夹则执行文件夹下所有的py文件

# def fn(path_):
#   '''
#       接受一个路径参数，如果该路径是一个文件，则执行这个文件，如果该路径是一个文件夹则执行文件夹下所有的py文件
#   '''
#     if os.path.isdir(path_):
#         lis = os.listdir(path_)
#         for file in lis:
#             tul = os.path.splitext(file)
#             print(file)
#             if tul[1] == '.py':
#                 os.system('python ' + os.path.join(path_, file))
#     else:
#         os.system('python ' + path_)


# 2.定义一个文件拷贝函数

# def file_copy(src_path, des_path):
#     '''
#         拷贝文件
#     '''
#     file_base_name = os.path.basename(src_path)
#     print(file_base_name)
#     if os.path.exists(os.path.join(des_path, file_base_name)):
#         print('目标位置已有该文件')
#     else:
#         if os.path.isfile(src_path):
#             with open(src_path, mode='rb') as src_file_stream,\
#                     open(os.path.join(des_path, file_base_name), mode='wb') as des_file_stream:
#                 ret = src_file_stream.read()
#                 des_file_stream.write(ret)

# 3.定义一个获取某个文件的上一级目录


# def get_last_dir(path_):
#     abs_path = os.path.abspath(path_)
#     if os.path.exists(abs_path):
#         file_dir = os.path.split(abs_path)[0]
#         last_dir = os.path.split(file_dir)[0]
#         print(last_dir)
#         return last_dir


# 4.使用os模块创建目录

# def makedir():
#     os.mkdir('test_file_two/glance')
#     os.chdir('test_file_two/glance')
#     open('__init__.py', mode='w')
#     print(os.getcwd())
#     os.mkdir('api')
#     open('api/__init__.py', mode='w')
#     open('api/policy.py', mode='w')
#     open('api/versions.py', mode='w')
#     os.mkdir('cmd')
#     open('cmd/__init__.py', mode='w')
#     open('cmd/manage.py', mode='w')
#     os.mkdir('db')
#     open('db/__init__.py', mode='w')
#     open('db/models.py', mode='w')

# 5.实现一个注册和登录功能py，注册信息使用字典格式保存到文件userinfo文件中

def register(userName, password):

    dic = {'user_name': userName, 'pwd': password}
    with open('userInfo', mode='ab') as file_stream:
        pickle.dump(dic, file_stream)


def check(userName):
    with open('userInfo', mode='rb') as file_stream:
        while True:
            try:
                dic = pickle.load(file_stream)
                if dic.get('user_name') == userName:
                    return 1
            except EOFError:
                return 0


def login(userName, password):
    with open('userInfo', mode='rb') as file_stream:
        while True:
            try:
                dic = pickle.load(file_stream)
                if dic.get('user_name') == userName and dic.get('pwd') == password:
                    return 1
            except EOFError:
                return 0


def register_login():
    userName = input('欢迎登录XXX系统,请输入用户名:')
    password = input('请输入密码:')
    if login(userName, password):
        print('登录成功')
    else:
        print('登录失败,请输入编号进行选择:')
        print('1--注册')
        print('0--退出系统')
        userChoice = input('请输入选择:')
        if userChoice == '1':
            userName = input('请输入用户名:')
            while True:
                if check(userName):
                    userName = input('用户名已存在,请重新输入:')
                else:
                    break
            password = input('请输入密码:')
            register(userName, password)
            if login(userName, password):
                print('注册成功')
            else:
                print('注册失败')
        elif userChoice == "0":
            print('退出系统')
        else:
            print('退出系统')


# 6.发红包
# def red_envelope(money, n):
#     lis = []
#     if n > 1:
#         avg = money / n
#         num = random.uniform(avg / 2, 1.5 * avg)
#         lis.append(num)
#         money = money - num
#         lis_inner = red_envelope(money, n - 1) #递归
#         lis.extend(lis_inner) #将每一次递归返回的结果extend到一个列表中去
#     elif n == 1:
#         lis.append(money)
#     return lis


# 7.计算器

def add_one(str_):
    return eval(str_)


def calculation(str_):
    # lis_ret = []
    # 匹配带括号的所有运算
    pattern_two = r'[(]\s*\d+(.\d+)?\s*[+\-*/]\s*[+-]?\d+(.\d+)?\s*[)]'
    pattern_one = r'\d+(.\d+)?\s*[*/]\s*[+-]?\d+(.\d+)?'  # 匹配出整数和小数的乘除法
    while re.search(pattern_one, str_):
        ret_one = re.search(pattern_one, str_).group()
        str_ = re.sub(pattern_one, str(eval(ret_one)), str_, count=1)
        print(str_)
    while re.search(pattern_two, str_):
        ret = re.search(pattern_two, str_).group()
        str_ = re.sub(pattern_two, str(eval(ret)), str_, count=1)
        print(str_)
    return eval(str_)


if __name__ == '__main__':

    # fn(r'H:\BaiduNetdiskDownload\OneDrive\PythonCode\老男孩Python全栈开发\day19_序列化模块_json_pickle\test_file')
    # file_copy(r'test_file\test_two.py', r'test_file_two')
    # get_last_dir('练习.py')
    # makedir()

    # 注册/登录功能
    register_login()

    # 发红包功能
    # lis = red_envelope(100, 2)
    # count = 0
    # for i in lis:
    #     count += i
    # print(count)
    # print(lis)
    # print(add_one('3 + 2'))
    # string = '1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2)'
    # # print(string.strip())
    # ret = calculation(string)
    # print(ret)
