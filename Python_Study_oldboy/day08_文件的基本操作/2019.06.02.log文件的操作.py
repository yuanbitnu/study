## 需要将log文件中的数据读取出来并按照相应的要求写入到一个字典
with open('2019.06.02.log',mode = "r",encoding = 'utf-8') as log_stream,\
	open("2019.06.02_副本.log",mode = 'w',encoding = 'utf-8') as new_log_stream:
	lis = ['Id','name','tel_num','car_name']
	for line in log_stream:
		line_lis = line.strip().split(",")
		lis_zip = zip(lis,line_lis)
		new_log_stream.write(str((dict(lis_zip)))+"\n")
		new_log_stream.flush()
