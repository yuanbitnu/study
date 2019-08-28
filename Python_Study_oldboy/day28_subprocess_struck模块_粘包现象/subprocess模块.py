import subprocess
#  subprocess模块用来生成子进程，连接子进程的的输入、输出、错误管道，并捕获其中的数据。
#  https://www.jb51.net/article/142787.htm
'''
一、subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, capture_output=False, 
    shell=False, cwd=None, timeout=None, check=False, encoding=None,
    errors=None, text=None, env=None, universal_newlines=None)

    1.args  需要执行的命令,类型为字符串或列表(命令和需要的参数)
    2.stdin、stdout(outputd别称)、stderr 执行的子程序的标准输入、输出和标准错误文件句柄，常用参数为PIPE，表事新建一个对子进程的管道，
        用来对子进程输入或者捕获子进程输出(stdout,正常输出|stderr，错误输出)，如果stderr的值为STDOUT，则表示stderr和
        stdout的输出都共用stdout
    3.shell 用来指定是否调用shell程序执行命令，为True时 args建议为字符串而不是序列
    4.encoding、errors、text 用来为stdin、stdout、stderr指定打开模式，为True以文本模式打开，false以二进制文件打开
    5.capture_output  是否对stdout、stderr进行捕获，为True时，不能再单独设置stdout、stderr的值，为False则不捕获，可以
        单独设置stdout、stderr是否捕获管道数据
    6.timeout  子进程的超时秒数
    7.env  为子进程单独设置环境变量，为False则表示继承主进程环境变量
    8.cwd  用于创建子进程的指令
    9 check  设为 True, 并且进程以非零状态码退出(0表示正常退出), 一个 CalledProcessError 异常将被抛出.
    10.universal_newlines和text一样指定标准输入输出的打开模式，text是universal_newlines的别名
'''
'''
一、subprocess.run()方法，推荐的调用子进程的方式是在任何它支持的用例中使用 run() 方法，返回一个completedProcess对象
    内部封装了 args(启动子进程的参数)、returncode(子进程的退出状态码)、check_returncode()(returncode非零则抛出异常)、
    stdout(捕获到的子进程的标准输出)、stderr(捕获到的子进程的标准错误)
'''

# completedProcess_instance = subprocess.run(
#     'ipconfig /all', capture_output=True, text=True, shell=True)
# print(completedProcess_instance.stdout)  # 打印正确输出
# print(completedProcess_instance.stderr)  # 打印错误输出

# 二、subprocess.call()方法  返回命令的执行结果和执行状态(0或者非0),执行结果输出到控制台，执行状态返回

# ret = subprocess.call('ipconfig /all')
# print(ret, type(ret))  #result = 0 <class 'int'>

# 三、subprocess.getstatusoutput(cmd),内部使用shell程序执行命令，返回执行状态和执行结果的元组(exitcode, output)

# ret = subprocess.getstatusoutput('ipconfig')
# print(ret)

# 四、subprocess.getoutput(cmd)  接受字符串形式的命令，返回执行结果,内部是通过调用getstatusoutput(cmd)[1]方法实现
# ret = subprocess.getoutput('ipconfig/all')
# print(ret)

# 五、subprocess.check_output()内部调用run()方法执行命令(check设置为True)，返回结果(run().stdout)，执行错误则抛出异常
# ret = subprocess.check_output('ipconfig /all')
# print(ret.decode('gbk')) # utf-8 不能对其返回值进行解码
