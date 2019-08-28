##列表推导式
#1、过滤掉长度小于3的字符串列表，并将剩下的转换成大写字母
lis = [s.upper() for s in ['dadada','ss','a','你好','石门柑橘'] if len(s) >= 3]
print(lis)

#2、求(x,y)其中x是0-5之间的偶数，y是0-5之间的奇数组成的元组列表
lis = [(x,y) for x in range(0,6) if x % 2 == 0 for y in range(0,6) if y % 2 !=0]
print(lis)

#3、求M中3，6，9组成的列表，M = [[1,2,3],[4,5,6],[7,8,9]]
M = [[1,2,3],[4,5,6],[7,8,9]]
lis  = [max(i) for i in M ]
print(lis)

#4、求50以内能被3整出的数的平方，并放入一个列表中
lis = [i **2 for i in range(0,50) if i % 3 == 0]
print(lis)

#5、构建一个列表['python1期','python2期','python3期','python4期']
lis = ['pyton%s期'%str(i) for i in range(1,16)]
print(lis)

#6、构建一个列表[(0,1),(1,2),(2,3),(3,4),(4,5),(5,6)]
lis = [tup for tup in zip(range(0,6),[1,2,3,4,5,6])]
print(lis)

#7、构建一个列表[0,2,4,6,8,10,12,14,16,18]
lis = [i for i in range(0,20,2)]
print(lis)

#8、将一个列表['alex','WuSir','老男孩','太白']构建成['alex0','WuSir1','老男孩2','太白3']
s_lis = ['alex','WuSir','老男孩','太白']
lis = ['%s%s'%(s,str(s_lis.index(s))) for s in s_lis]
print(lis)