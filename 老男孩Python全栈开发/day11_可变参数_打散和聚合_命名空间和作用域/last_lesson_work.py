##定义一个参数必须是列表的函数,功能为将列表的index和value组成一个键值对加入一个字典并返回
# def fn1(lis:list) ->dict:
# 	dic = {}
# 	for i in range(0,len(lis)):
# 		dic[i] = lis[i]
# 	return dic

# lis = [12,5,14,6,8,32]
# print(fn1(lis))


##定义一个接收"姓名,性别,年龄,学历"4个参数的函数,用户通过输入这四个内容,并将其传递给函数,此函数将内容保存进一个student_msg的文件中去
# import os
# def write_fiel(name,age,education,gander = '男'):
# 	if not os.path.exists('student_msg.txt'):
# 		with open('student_msg.txt',mode = 'w',encoding = 'utf-8') as file_stream:
# 			file_stream.write('name:%s,age:%s,education:%s,gander:%s\n'%(name,age,education,gander))
# 			file_stream.flush()
# 	else:
# 		with open('student_msg.txt',mode = 'a',encoding = 'utf-8') as file_stream:
# 			file_stream.write('name:%s,age:%s,education:%s,gander:%s\n'%(name,age,education,gander))
# 			file_stream.flush()
# while True:
# 	name = input('请输入姓名:')
# 	gander = input('请输入性别:')
# 	age = input('请输入年龄:')
# 	education = input('请输入学历:')
# 	if gander =='女':
# 		write_fiel(name,age,education,gander)
# 	else:
# 		write_fiel(name,age,education)
# 	other = input('输入"Q"或者"q"退出程序,输入其他任意字符程序继续')
# 	if other in ['Q','q']:
# 		break

##定义注册和三次登录验证两个函数,用户名和密码保存在userName_pwd.txt中
def regist(name,pwd):
	'''
		注册用户名和密码,用户名必须唯一
	'''
	lis = []
	with open('userName_pwd.txt',mode = 'a+',encoding = 'utf-8') as file_stream:
		file_stream.seek(0)
		for line in file_stream:
			
			if line.strip() == '':
				file_stream.write("userName:%s|pwd:%s\n"%(name,pwd))
				file_stream.flush()
				break
			else:
				lis_one =  line.strip().split("|")
				user_name = lis_one[0].strip().split(':')[1]
				lis.append(user_name)
		if name in lis:
			return False
		else:
			file_stream.write("userName:%s|pwd:%s\n"%(name,pwd))
			file_stream.flush()
			return True

def authenticate(user_name:str,pwd:str) ->bool:
	'''
		验证用户名和密码,正确返回True,错误返回False
	'''
	import os
	if not os.path.exists('userName_pwd.txt'):
		return False
	else:
		dic = {}
		with open('userName_pwd.txt',mode = 'r',encoding = 'utf-8') as file_stream:
			for line in file_stream:
				if line.strip() == '':
					return False
				else:
					lis_one = line.strip().split('|')
					userName = lis_one[0].strip().split(':')[1]
					password = lis_one[1].strip().split(':')[1]
					dic[userName] = password
		if dic.get(user_name) != None and dic[user_name] == pwd:
			return True
		else:
			return False
						 




def log():
	'''
		三次验证登录,正确返回True,错误三次返回False
	'''
	count = 0
	while count < 3:
		user_name = input('请输入用户名:')
		pwd = input('请输入密码')
		if authenticate(user_name,pwd):
			print("登录成功")
			count = 0
			return True
		else:
			count += 1
			if count <= 2:
				print("账号密码不匹配,请重新输入")
	print('错误三次,登录失败')
	return False


	
# print(regist('王五','ww'))
# print(authenticate('王五','ww'))
# log()
