def my_get_suffix(filename,has_dot = False):
	file_len = len(filename)
	star_index = -1
	index = 0
	for _ in range(file_len):
		if filename[star_index] == ".":
			index = star_index
			break
		star_index += -1
	if has_dot:
		suffix  = filename[index:]
	else:
		suffix = filename[index+1:]
	return suffix


def get_suffix(filename,has_dot = False):
	posi = filename.rfind('.')
	index = posi if  (0 < posi < len(filename) -1 and has_dot) else posi+1
	return filename[index:]


suffix =  my_get_suffix('aa.aaa.doc',True)
print(suffix)

suffix = get_suffix('11111.doc.rar',True)
print(suffix)