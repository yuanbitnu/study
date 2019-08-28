def get_max_second(lis):
	m,s = (lis[0],lis[1]) if lis[0] > lis[1] else (lis[1],lis[0])
	for ele in lis[2:len(lis)]:
		if ele > m:
			s = m
			m = ele
		elif ele > s:
			s = ele
	return m,s

lis = [5,3,2,7,5,32,1]
m,s = get_max_second(lis)
print(f'max = {m}; second = {s}')