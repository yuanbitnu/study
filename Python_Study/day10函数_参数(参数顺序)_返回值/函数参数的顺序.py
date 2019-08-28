# 参数
# 	1.实参
# 		位置参数
# 		关键字参数
# 		混合参数(先位置,后关键字)
# 	2.形参
# 		位置参数
# 		默认值参数
# 		可变参数:
# 			*args:接收位置参数的可变参数
# 			**kwargs:接收关键字参数的可变参数
# 		形参的顺序:位置参数,*args,默认值参数,**kwargs

def fn(name,*do_something,addr = '北京',**something):
	print(name)
	print(do_something)
	print(addr)
	print(something)

fn('张三','吃','玩',addr = '河北',food = '北京烤鸭',play = '八达岭长城')