# print(1 > 2 and 3 or 6)

# ???
# lis = [1,2,3,4,5]
# print(lis[3:1])

# ##将字符传转化为列表
# str = '1,2,3'
# lis = str.split(',')
# print(lis)

# ##将列表变成字符串
# lis = ['1','2','3']
# str = ','.join(lis)
# print(str)

# 使用range()打印100,99,98,...1,0
# for i in range(100,-1,-1):
# 	print(i)

# 计算1-3+5-7+9-11....的结果

# 方式一
# i = 1
# j = 0
# result = 0
# while i < 100:
# 	if i % 2 != 0:
# 		j += 1
# 		if j %2 == 0:
# 			result -= i
# 		else:
# 			result += i
# 	i += 1
# print(result)

# 方式二 通过改变运算符
# result = 0
# operator = 1
# for i in range(1,100,2):
# 	result = result + i * operator
# 	operator = - operator
# print(result)

# 将字符串'jay:周杰伦|jj:林俊杰|gg:太白|sb:alex'处理成字典{'jay': '周杰伦', 'jj': '林俊杰', 'gg': '太白', 'sb': 'alex'}
# str = 'jay:周杰伦|jj:林俊杰|gg:太白|sb:alex'
# lis = str.strip().split("|")
# dic = {}
# for item in lis:
# 	lis_1 = item.strip().split(':')
# 	dic.update({lis_1[0]:lis_1[1]})
# print(dic)

# 实现一个整数加法计算器,并将最后结果替换字典{'最终计算结果':None}中的None
# content =  input('请输入内容:')
# content = content.replace(' ','')
# dic = {'最终计算结果':None}
# result = 0
# lis = content.strip().split("+")
# if len(lis) < 2:
# 	print('请最少输入两个数相加')
# else:
# 	for i in lis:
# 		result +=int(i)
# 	dic['最终计算结果'] = result
# 	print(dic)

# 敏感词过滤
# lis =  ['老大不小','少','高','大']
# while True:
# 	content = input('请输入内容')
# 	content = content.replace(' ','').strip()
# 	for item in lis:
# 		if item in content:
# 			content = content.replace(item,'*'*len(item))
# 	print(content)

# 各省车牌数量统计
# cars = ['鲁A32444','鲁B12333','京B8989M','黑C49678','黑C46555','沪B25041','黑C34567']
# locations = {'鲁':"山东",'沪':'上海','京':'北京','黑':'黑龙江','粤':'广东','湘':'湖南'}
# dic = {}
# for car in cars:
# 	simp =  car[0]
# 	province = locations[simp]
# 	if dic.get(province) == None:
# 		dic[province] = 1
# 	else:
# 		dic[province] += 1
# print(dic)

# 字典转化
lis3 = [
    {'name': 'alex', 'hobby': '抽烟'},
    {'name': 'alex', 'hobby': '喝酒'},
    {'name': 'alex', 'hobby': '烫头'},
    {'name': 'alex', 'hobby': 'Message'},
    {'name': 'wusir', 'hobby': '唱歌'},
    {'name': 'wusir', 'hobby': '街舞'},
    {'name': 'alex', 'hobby': '打架'},
    {'name': '太白', 'hobby': '溜达'},
    {'name': 'wusir', 'hobby': '画画'}
]
# new_lis = []
# for dic in lis3:
# 	if len(new_lis) == 0:
# 		new_lis.append({'name':dic.get('name'),'hobby':[dic.get('hobby')]})
# 	else:
# 		state = False
# 		for new_dic in new_lis:
# 			if dic.get('name') == new_dic.get('name'):
# 				state = True
# 				new_dic.get('hobby').append(dic.get('hobby'))
# 		if state == False:
# 			new_lis.append({'name':dic.get('name'),'hobby':[dic.get('hobby')]})

# print(new_lis)

new_lis = []
for dic in lis3:
    if len(new_lis) == 0:
        new_lis.append({'name': dic.get('name'), 'hobby': [dic.get('hobby')]})
    else:
        for new_dic in new_lis:
            if dic.get('name') == new_dic.get('name'):
                new_dic.get('hobby').append(dic.get('hobby'))
                break
        else:
            new_lis.append(
                {'name': dic.get('name'), 'hobby': [dic.get('hobby')]})
print(new_lis)

# list4= []

# for ren in list3: # {"name": "alex", "hobby": "抽烟"},
#     for el in list4:
#         if el['name'] == ren['name']:
#             el['hobby_list'].append(ren['hobby'])
#             break
#     else:
#         dic = {}
#         dic['name'] = ren['name']
#         dic['hobby_list'] = [ren['hobby']]
#         list4.append(dic) # 第一个人进去
# print(list4)
