##读文件并打印出来
# with open('a1.txt',mode = 'r',encoding = 'utf-8') as file_stream:
# 	for line in file_stream:
# 		print(line.strip())

##在源文件后面追加一行内容
# with open('a1.txt',mode = 'a',encoding = 'utf-8') as file_stream:
# 	file_stream.write('\n信不信由你,反正我信了')
# 	file_stream.flush()

##将源文件全部都出来，并且在后面添加一行内容
# with open('a1.txt',mode = 'r+',encoding = 'utf-8') as file_stream:
# 	for line in file_stream:
# 		print(line.strip())
# 	file_stream.write('\n信不信由你,反正我信了')

##将源文件全部清空，并换成以下内容（每天坚持一点，每天努力一点，每天多思考一点）
# with open('a1.txt',mode = 'w+',encoding = 'utf-8') as file_stream:
# 	file_stream.write('每天坚持一点，\n每天努力一点，\n每天多思考一点\n')
# 	file_stream.flush()


#修改文件内容,在某一行后面添加新内容，并保存
# import os
# with open('a1.txt',mode = 'r',encoding = 'utf-8') as file_stream,\
# 	open('a1_副本.txt',mode = 'w',encoding = 'utf-8') as new_file_stream:
# 	for line in file_stream:
# 		if line.strip() == '每天多思考一点,':
# 			new_file_stream.write(line)
# 			new_file_stream.write('慢慢你会发现\n')
# 			new_file_stream.flush()
# 		new_file_stream.write(line)
# 		new_file_stream.flush()
# os.remove('a1.txt')
# os.rename('a1_副本.txt','a1.txt')

##***************************************************************
##***************************************************************

##以r+模式打开源文件，判断源文件是否可读，是否可写
# with open('a1.txt',mode = 'r+',encoding = 'utf-8') as file_stream:
#  	if file_stream.readable(): ##在表达式为假的情况下才会判断elif中的语句
#  		print('文件是可读的')
#  	# elif file_stream.writable():##此时elif不会执行
#  	# 	print('文件是可写的')
#  	if file_stream.writable():
#  		print('文件是可写的')


##以r的模式打开源文件,使用for循环遍历文件句柄

# with open('a1.txt',mode = "r+",encoding = 'utf-8') as file_stream:
# 	for line in file_stream:
# 		print(line.strip())

##以r的模式打开源文件,使用readlines()方法读取文件,并且遍历期结果
# with open('a1.txt',mode = 'r+',encoding = 'utf-8') as file_stream:
# 	lines =  file_stream.readlines()  ##readlines()方法会一次性将整个文件的内容读取完,并以行为单位放进一个列表中,然后返回
# 	for line in lines:
# 		print(line.strip())

##以r的模式打开源文件,读取前四个字符
# with open('a1.txt',mode = 'r',encoding = 'utf-8') as file_stream:
# 	s = file_stream.read(4)
# 	print(s)

##以r的模式打开源文件,读取第一行内容,并去掉空格\制表符\换行符
# with open('a1.txt',mode = 'r',encoding = 'utf-8') as file_stream:
# 	line_one =  file_stream.readline().strip()
# 	print(line_one)


##以r的模式打开源文件,从"努力"开始读取,一直读到最后
# with open('a1.txt',mode = 'r',encoding = 'utf-8') as file_stream:
# 	file_stream.seek(29)
# 	s = file_stream.read()
# 	print(s)

##以a+的模式打开源文件,先追加一行,然后从最开始读取全部内容
# with open('a1.txt',mode = 'a+',encoding = 'utf-8') as file_stream:
# 	file_stream.write('老男孩教育')
# 	file_stream.seek(0)
# 	for line in file_stream:
# 		print(line.strip())

##使用truncate()方法截取源文件
# with open('a1.txt',mode = 'r+',encoding = 'utf-8') as file_stream:
# 	file_stream.seek(6) ## fileObject.seek(offset[, whence]) offset -- 开始的偏移量，也就是代表需要移动偏移的字节数
# 						## whence：可选，默认值为 0。给offset参数一个定义，表示要从哪个位置开始偏移；0代表从文件开头开始算起，
# 						## 1代表从当前位置开始算起，2代表从文件末尾算起。
# 	file_stream.truncate()
# 	## truncate() 截断文件,如果指定了可选参数 size，则表示截断文件为 size 个字符。 如果没有指定 size，则从当前位置起截断；截断之后 size 后面的所有字符被删除。
# 	file_stream.seek(0)
# 	s = file_stream.read()
# 	print(s)


##读取a.txt固定格式的文件,构建数据类型,并计算总价格
##格式
# apple 10 1
# tesla 10 1
##数据类型
# [{'name': 'apple', 'price': '10', 'amount': '1'}, {'name': 'tesla', 'price': '10', 'amount': '1'}]


# lis = []
# with open('a.txt',mode = 'r',encoding = 'utf-8') as file_stream:
# 	for line in file_stream:
# 		lis_inner = line.strip().split(" ")
# 		dic = {'name':lis_inner[0],'price':lis_inner[1],'amount':lis_inner[2]}
# 		lis.append(dic)
# print(lis)
# count = 0
# for item in lis:
# 	count += int(item.get('price')) * int(item.get('amount'))
# print(count)


##读取a2.txt固定格式的文件,构建数据类型,并计算总价格
##格式
# name:apple price:10 amount:1 year:2012
# name:tesla price:10 amount:1 year:2013
##数据类型
# [{'name': 'apple', 'price': '10', 'amount': '1', 'year': '2012'}, {'name': 'tesla', 'price': '10', 'amount': '1', 'year': '2013'}]
# lis = []
# with open('a2.txt',mode = 'r',encoding = 'utf-8') as file_stream:
# 	for line in file_stream:
# 		lis_inner = line.strip().split(" ")
# 		dic = {}
# 		#lis_tem=[]
# 		for item in lis_inner:
# 			lis_inner_two = item.split(":")
# 			dic[lis_inner_two[0]] = lis_inner_two[1]  ##两种方式加入字典：一是一个一个键值对的加入，而是将其组合成一个列表了使用dict(lis)函数直接转成字典
# 			#lis_tem.append(lis_inner_two)
# 		#lis.append(dict(lis_tem))
# 		lis.append(dic)
# print(lis)
# count = 0
# for item in lis:
# 	count += int(item.get('price')) * int(item.get('amount'))
# print(count)



