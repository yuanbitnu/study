## 实际上在当前文件本身是不能修改的,要实现修改的效果只能是将文件读取到内存中,在内存中修改完毕后写入到另一个"副本文件"
## 之后将源文件删除,将副本文件名改为当前文件名

import os

with open('待修改文件.txt',mode = "r",encoding = 'utf-8') as src_file_stream, \
	open('待修改文件_副本.txt',mode = "w",encoding = 'utf-8') as des_file_stream:
	for line in src_file_stream:
		line = line.replace('白居易','李白')
		des_file_stream.write(line)
		des_file_stream.flush()

os.remove('待修改文件.txt')
os.rename('待修改文件_副本.txt','待修改文件.txt')