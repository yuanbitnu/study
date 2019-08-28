import random

def generate_code(code_len):
	'''
		生成指定长度的验证码,验证码由大小写字母和数字构成
	'''
	all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	last_index = len(all_chars) -1
	code = ''
	for _ in range(code_len):
		index = random.randint(0,last_index)
		code = code + all_chars[index]
	return code

code =  generate_code(5)
print(code)