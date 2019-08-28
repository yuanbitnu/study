# os模块 用来和操作系统打交道
import os
# 一.系统操作
# print(os.sep)  # result = \  返回当前操作系统路径的分隔符

# print(os.name) #result = nt 返回当前工作的操作系统平台  windows为"nt" linux为"posix"

# print(os.getenv('PATH')) #获取环境变量

# print(os.getcwd()) #获取当前文件的路径

# 二.目录和文件的增删改查
# 1.增加单级目录
# os.mkdir('dir1')  # 创建一个目录,一次只能创建一级目录,创建多级目录抛出异常
# os.mkdir('dir3/dir4') # 一次创建多级目录抛出异常,该方法只会创建参数中的最后一级目录,并且创建的前提是所有上级目录已存在
# os.mkdir('dir1/dir2') #当dir1目录已经存在,此时传入此参数则可以正常创建dir2这个目录

# 2.增加多级目录
# os.makedirs('dir5/dir/6/dir7') #创建多级目录

# 3.删除单级目录
# os.rmdir('dir5/dir/6') #删除参数中最后一级空目录,如果目录中有文件则无法删除

# 4.删除多级目录
# os.removedirs('dir5/dir/6') #删除多级空目录,如果目录中有文件则无法删除

# 5.删除一个文件
# os.remove('222.txt') #删除一个文件


# 6.获取文件属性
# file_property = os.stat('time模块练习.py')
# print(type(file_property))  # result = <class 'os.stat_result'>
# print(file_property) #result = os.stat_result(st_mode=33206, st_ino=1970324837084034, st_dev=211383414, st_nlink=1, st_uid=0, st_gid=0, st_size=1474, st_atime=1560746107, st_mtime=1560861592, st_ctime=1560746107)

# 三.在python环境中运行shell命令(操作系统命令)
# 1. os.system()方法

# ret = os.system('dir') #没有返回值,用户在shell命令行界面直接显示,因此只适合做具体的操作
# print(ret) #result = 0

# 2. os.popen()方法,

# ret = os.popen("dir")
# print(type(ret))  # result = <class 'os._wrap_close'>
# print(ret.read())  # result 当前文件运行路径下得dir列表


# 四.路径操作os.path

# 1.os.path.abspath()方法，返回文件的绝对路径
# absolute_path = os.path.abspath('time模块练习.py') #返回文件的绝对路径
# print(absolute_path) # result = H:\BaiduNetdiskDownload\OneDrive\PythonCode\老男孩Python全栈开发\day18(random_time_sys_os模块)\time模块练习.py

# 2.os.path.isabs()方法，判断一个路径是否是绝对路径
# ret = os.path.isabs('time模块练习.py')
# print(ret)  # result = False

# ret = os.path.isabs(os.path.abspath('time模块练习.py'))
# print(ret)  #result = True


# 3.os.path.split(file_absolute),传入一个absolute路径的参数,分割文件名与目录（事实上，如果你完全使用目录，它也会将最后一个目录作为文件名而分离，同时它不会判断文件或目录是否存在）
# ret = os.path.split(os.path.abspath('time模块练习.py'))
# print(ret)  # result = ('H:\\BaiduNetdiskDownload\\OneDrive\\PythonCode\\老男孩Python全栈开发\\day18(random_time_sys_os模块)', 'time模块练习.py')

# ret = os.path.split('不存在的路径文件.py')
# print(ret)  # result = ('', '不存在的路径文件.py') ,不会检查改文件是否存在


# #尽管下面示例传入的参数仅仅只是一个目录,没有文件名,该方法还是会将最后一个目录作为文件名进行分割
# ret = os.path.split(
#     "'H:\\BaiduNetdiskDownload\\OneDrive\\PythonCode\\老男孩Python全栈开发\\day18(random_time_sys_os模块)")
# print(ret) # result = ("'H:\\BaiduNetdiskDownload\\OneDrive\\PythonCode\\老男孩Python全栈开发", 'day18(random_time_sys_os模块)')


# 4.os.path.splitext()方法,用来分割传入文件名参数的 文件名和扩展名,不会判断文件是否存在

# ret = os.path.splitext(os.path.abspath('time模块练习.py'))  # 参数为绝对路径
# print(ret)  # restule = ('H:\\BaiduNetdiskDownload\\OneDrive\\PythonCode\\老男孩Python全栈开发\\day18(random_time_sys_os模块)\\time模块练习', '.py')

# ret = os.path.splitext('time模块练习.py.px')
# print(ret)  # result = ('time模块练习.py', '.px') #找到传入字符创文件名的最后一个"."做分割,不会判断文件是否存在

# ret = os.path.splitext('time模块练习.py')
# print(ret) # result = ('time模块练习', '.py')


# 5.os.path.isfile(file_absolute),检查一个路径是否是一个文件
# ret = os.path.isfile(os.path.abspath('time模块练习.py')) #传入一个absolute路径
# print(ret) #result = True


# 6.os.path.isdir(file_absolute),检查一个路径是否是一个目录
# ret = os.path.isdir(os.path.abspath('time模块练习.py'))
# print(ret) #result = False


# 7.os.path.exists(file_absolute) ，检查一个目录或文件是否存在
# ret = os.path.exists(os.path.abspath('time模块练习.py'))
# print(ret) #result = True


# 8.os.path.dirname(absolute_file) 返回文件路径
# ret = os.path.dirname(os.path.abspath("time模块练习.py"))
# print(ret)  # result = H:\BaiduNetdiskDownload\OneDrive\PythonCode\老男孩Python全栈开发\day18(random_time_sys_os模块)


# # 9.os.path.basename(absolute_file) 返回文件名
# ret = os.path.basename(os.path.abspath('time模块练习.py'))
# print(ret) # result = time模块练习.py


# 10.os.path.join(path,*paths),在不同的参数中间加入"/"符号,组成一个路径
# ret = os.path.join(os.path.dirname(
#     os.path.abspath('time模块练习.py')), 'time模块练习.py')
# print(ret) # result = H:\BaiduNetdiskDownload\OneDrive\PythonCode\老男孩Python全栈开发\day18(random_time_sys_os模块)\time模块练习.py
