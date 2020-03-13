import sys
import os
# sys.path.append(os.path.dirname(os.path.dirname(__file__)))
project_path = os.path.dirname(os.path.dirname(__file__))
# print(project_path)
sys.path.append(project_path)
# sys.path.insert(0,project_path)
print(sys.path)
from core import staff_operate, login_verification
from lib import general


def main():
    while True:
        print('登陆：')
        user = input('请输入用户名：')
        pwd = input('请输入密码')
        while not login_verification.login(user, pwd):
            print('用户名或密码错误，请重新输入：')
            user = input('请输入用户名：')
            pwd = input('请输入密码')
        while login_verification.login(user, pwd):
            print('1:增')
            print('2:删')
            print('3:查')
            print('4:改')
            print('q:退出')
            user_choice = input('请选择需要的操作：')
            if user_choice == '1':
                user_cmd = input('请输入命令：')
                staff_operate.update_staff(user_cmd)
                staff_operate.display_staff()
            elif user_choice == '2':
                user_cmd = input('请输入命令：')
                staff_operate.delete_staff(user_cmd)
                staff_operate.display_staff()
            elif user_choice == '3':
                user_cmd = input('请输入命令：')
                staff_operate.select_staff(user_cmd)
            elif user_choice == '4':
                user_cmd = input('请输入命令：')
                staff_operate.set_staff(user_cmd)
                staff_operate.display_staff()
            else:
                break


if __name__ == '__main__':
    main()
