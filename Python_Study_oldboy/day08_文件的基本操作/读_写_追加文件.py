##读文件

# with open('文本文件.txt',mode = 'r',encoding = 'utf-8') as file_stream:
# 	for line in file_stream:
# 		print(line.strip())

##写文件,只要进行操作,一定会先自动清空,再写入.

# with open('文本文件.txt',mode = 'w',encoding = 'utf-8') as file_stream:
# 	file_stream.write('窗前明月光,\n')
# 	file_stream.write('疑似地上霜.\n')
# 	file_stream.write('举头望明月,\n')
# 	file_stream.write('低头思故乡.\n')
# 	file_stream.write("\n\n作者: 李白")


# with open('文本文件.txt',mode = 'r',encoding = 'utf-8') as file_stream:
# 	for line in file_stream:
# 		print(line.strip())


##append追加文件


# with open('文本文件.txt',mode = 'a',encoding = 'utf8') as file_stream:
# 	file_stream.write('\n朝代: 唐朝')

# with open('文本文件.txt',mode = 'r',encoding = "utf-8") as file_stream:
# 	for line in file_stream:
# 		print(line.strip())