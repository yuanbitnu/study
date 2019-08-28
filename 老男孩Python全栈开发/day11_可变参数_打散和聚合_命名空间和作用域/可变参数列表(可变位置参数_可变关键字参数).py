# def commodity_lis(*commodity): ## *号表示接受位置参数的动态传参,会将接收到的多个参数转为tuple赋值给commodity
# 							   ## 可变参数必须位于参数列表最后
# 	print(commodity) 

# commodity_lis('铅笔','钢笔','橡皮檫')  ##result = ('铅笔', '钢笔', '橡皮檫')
# commodity_lis('西红柿')  ##result = ('西红柿',) ##单个元素的元祖,在那一个元素后面得添加","号
# commodity_lis()  ##result = ()  ##没有传参时,将会构建一个空元祖

##****************************************************************************

# def commodity_lis(**commodity): ## **号表示接收关键字参数的动态传参,会将接收到的关键字参数装包成dict复制给commodity
# 	print(commodity)

# commodity_lis(fruit = 'apple',drink = 'water',food = '煲仔饭')  ##result = {'fruit': 'apple', 'drink': 'water', 'food': '煲仔饭'}
# commodity_lis(fruit = 'apple')  ##result = {'fruit': 'apple'}
# commodity_lis()  ##result = {} ##没有传参时,将会构建一个空字典

a =10
def fn():
	b = a
	b = 20
fn()
print(a)