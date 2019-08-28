import sys
# sys模块是和python解释器打交道的
# sys 模块的方法：
# 一. sys.argv 返回命令行界面 python 命令后面输入的内容保存进一个列表中，(这些内容可以作为参数等)
# 类似于用户使用input()函数向程序输入

# print(sys.argv)


# 二、sys.path 是python搜索模块的路径集，保存在一个list中

 print(sys.path)


# 三、sys.modules  是我们导入到内存中的所有模块的名字：或者说是这个模块的内存地址
print(sys.modules['sys'].path)
