## r+模式从头开始读起,但不管是否读完,只要在进行写入时光标会移动到整个文档尾部,从尾部还是写入

# with open('文本文件.txt',mode = 'r+',encoding = 'utf-8') as file_stream:
	##一.先读再写 r+模式从头开始读起,光标从头开始到读到的位置,但不管是否读完,只要在进行写入时光标会移动到整个文档尾部,从尾部还是写入
	# s = file_stream.read(5) #读取5个字符
	# print("读取的内容:",s,end = "")
	# file_stream.write('\n白毛浮绿水,')
	# s1 = file_stream.read(10)
	# print("读取的内容:",s1)
	# file_stream.seek(0) #将贯标移动到文档首部 seek(偏移量,0),第二个参数0表示文档首部,1表示光标当前所在位置,2表示文档尾部
	# for line in file_stream:
	# 	print(line.strip())

	##二.先写再读  因为是R+因此光标开始的位置在文档首部,此时写入内容则会覆盖文档首部的内容
	# file_stream.write('红掌拨清波')
	# file_stream.flush()
	# for line in file_stream:
	# 	print('读取到的内容',line.strip())


## W+写读模式,先写后度,只要进行操作,一定会先清空内容,在写和读.

# with open('文本文件.txt',mode = "w+",encoding = 'utf-8') as file_stream:
# 	file_stream.write('床前明月光,\n疑似地上霜.\n举头望明月,\n低头思故乡.\n') #写完以后光标位于文档尾部
# 	file_stream.flush()
# 	file_stream.seek(0) #因为光标位于文档尾部,因此想要读出文档内容需要使用seek(0)方法将光标移到文档首部
# 	for line in file_stream:
# 		print(line.strip())

## a+追加写读模式,先写后度,因为是append(追加),因此不会将文档内容清空,且光标位于文档尾部

with open('文本文件.txt',mode = 'a+',encoding = 'utf-8') as file_stream:
	file_stream.write('\n作者: 李白')
	file_stream.flush()
	file_stream.seek(0)
	for line in file_stream:
		print(line.strip())








