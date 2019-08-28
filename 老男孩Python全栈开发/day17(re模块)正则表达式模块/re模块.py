# regular expression re模块用来操作正则表达式
import re
# ***********************************************************************
# 一、常用方法

# 1、re.findall()方法,将字符串中所有被regular expression匹配的内容放入一个list中返回

# pattern = r'\d{3}' #匹配三位正整数
# string = 'jkh983khj12jhh645jjk2jhk6k'
# lis = re.findall(pattern,string)
# print(lis)  ##result = ['983', '645']


# 2、re.search()方法,将指定字符串中第一个被regular expression匹配的内容放入一个re.Match对象中返回,如果没有匹配内容则返回None

# pattern = r'(\d{2,})' #匹配至少两位数的正整数
# string = 'jkh789khj12jhh64jjk2jhk6k'
# ret = re.search(pattern,string)
# print(ret) ## result = <re.Match object; span=(3, 5), match='98'>
# if ret: ##re.search()方法如果没有匹配到内容则返回None,为None的情况调用re.Match.group()方法会抛出异常,因此需要做一个判断
# 	print(ret.group()) ## re.group(0)与ret.group()等价  result = 983


# 3、re.match()方法,和search()方法类似,返回第一个匹配内容,放入re.Match对象中返回,但match()方法默认在传入的regular expression前加了一个'^',表示字符串开头需要完全匹配

# pattern = r'\d{2,}' #匹配至少两位数的正整数
# string = '983khj12jhh645jjk2jhk6k'
# ret = re.match(pattern,string)  ##如果re.match()没有匹配到内容则返回None,为None的情况下调用re.Match()方法会抛出异常,因此需要做一个判断
# print(ret)
# if ret:
# 	print(ret.group()) ##result = 983


# 4、re.split()方法,类似于字符串中split方法(按照指定的内容分割字符串)re模块中的split方法则是按照"正则表达式匹配的内容"进行分割,返回分割后的list

# pattern = r'\d+' #匹配正整数
# string = 'jkh789khj12jhh64jjk2jhk6k'
# lis = re.split(pattern,string)
# print(lis) ## result = ['jkh', 'khj', 'jhh', 'jjk', 'jhk', 'k']  此时作为分隔符的内容被去掉了

# 5、re.sub()方法,类似于字符串中replace()方法(使用指定内容替换指定内容),re模块中的sub方法则是使用指定内容替换正则表达式匹配的内容,返回新的字符串

# pattern = r'\d+'
# string = 'jkh789khj12jhh64jjk2jhk6k'
# new_str = re.sub(pattern,'--',string)
# print(new_str)  ##result = jkh--khj--jhh--jjk--jhk--k


# 6、re.subn()方法,和sub方法一样,使用指定内容去替换正则表达式匹配的内容,同时返回替换的次数

# pattern = r'\d+'
# string = 'jkh789khj12jhh64jjk2jhk6k'
# new_str = re.subn(pattern,'--',string)
# print(new_str) ##result = ('jkh--khj--jhh--jjk--jhk--k', 5)


# 7、re.compile()方法，可以将regular expression一次编译多次执行，降低程序的时间复杂度
# pattern = r'\d+'
# pattern_compile =  re.compile(pattern)
# print(pattern_compile)  ## result = re.compile('\\d+')
# string = 'jkh789khj12jhh64jjk2jhk6k'
# new_str = pattern_compile.subn('--',string)
# print(new_str)  result = ('jkh--khj--jhh--jjk--jhk--k', 5)

# 8、re.finditer()方法,可以将regular expression 匹配的结果以re.Match对象的形式放入一个iterator迭代器中,降低程序的空间复杂度

# pattern = r'\d+'
# pattern_compile = re.compile(pattern) ##使用re.compile()方法降低时间复杂度
# string = 'jkh789khj12jhh64jjk2jhk6k'
# genetator =  pattern_compile.finditer(string)  ##使用re.finditer()方法降低了空间复杂度
# print(genetator)  ##result = <callable_iterator object at 0x0000022D34E9F320>
# if '__iter__' in dir(genetator):
# 	for item in genetator:    ##每一个item都是一个re.Match对象
# 		print(item.group(0))  ##通过re.Match.group([0])调用取值


# ***********************************************************************
# 二、python中regular expression中"()"分组符号的优先级问题,在分组符号内部的开头加上"?:"取消分组优先级

# 1、re.findall()优先级问题,带分组符的正则匹配部分被优先匹配

# s = 'jkh98.023khj12jhh64.5jjk2jhk6k'
# ## 下面regular expression匹配所有正整数和正小数
# pattern_one = r'\d+(\.\d+)*' ##因为在regular expression中使用了"()"分组符号,而在python中规定了优先显示'()'分组符号中匹配的内容
# lis_one =  re.findall(pattern_one,s)
# print(lis_one) ##result = ['.023', '', '.5', '', '']

# pattern_two = r'\d+(?:\.\d+)*' ##在被分组的正则表达式前面加上'?:'则取消了分组符的优先级,会按照正则表达式正常匹配进行返回
# lis_two = re.findall(pattern_two,s)
# print(lis_two) ##result = ['98.023', '12', '64.5', '2', '6']

# pattern_three = r'(\d+)(\.\d+)*'
# lis_three = re.findall(pattern_three,s)  ##result = [('98', '.023'), ('12', ''), ('64', '.5'), ('2', ''), ('6', '')]
# ##以上结果是因为在'\d+'位置也添加了分组,实际上整个正则表达式第一项匹配的应该是98.023,但因为分组优先的原因,python
# ##会将这个结果拆分为符合(\d+)和(\.\d+)*这两个结果进行显示,而整个又是一条正则,因此使用元祖括起来,正整数的元素也因为()
# ##分组符的原因要求显示(\.\d+)*部分,因此显示为空
# print(lis_three)


# 2、re.split()分组问题,带分组符的匹配部分在切割后会被保留下来


# pattern_one = r'\d+(?:\.\d+)*' #匹配正整数,此处的分组是该regular expression本身就需要的,因此完全按照正则规则匹配则需要取消()分组的优先级
# string = 'jkh98.023khj12jhh64.5jjk2jhk6k'
# ret = re.split(pattern_one,string)
# print(ret)  ##result = ['jkh', 'khj', 'jhh', 'jjk', 'jhk', 'k']


# pattern_two = r'\d+(\.\d+)*' #匹配正整数,此处会按照整个正则表达式匹配的内容进行分割,但保留的只是该正则表达式有分组符的部分,
# 								##如果该分组部分有匹配内容则返回该内容,如果没有则返回None
# string = 'jkh98.023khj12jhh64.5jjk2jhk6k'
# ret = re.split(pattern_two,string)
# print(ret)  ##result = ['jkh', '.023', 'khj', None, 'jhh', '.5', 'jjk', None, 'jhk', None, 'k']


# pattern_three_one = r'(\d+(\.\d+)*)' ##对整个正则人为加上了分组,但内部分组优先级依然存在
# pattern_three_two = r'(\d+(?:\.\d+)*)' ##对整个正则认为加上了分组,同时将其内部分组优先级取消了
# string = 'jkh98.023khj12jhh64.5jjk2jhk6k'
# ret_three_one = re.split(pattern_three_one,string)
# print(ret_three_one)  ## result =['jkh', '98.023', '.023', 'khj', '12', None, 'jhh', '64.5', '.5', 'jjk', '2', None, 'jhk', '6', None, 'k']
# ##针对第一种两个分组都存在的情况,split()方法会保留两个分组分别匹配的被切割的内容,如果某个分组内没有被匹配上的则返回None


# ret_three_two =  re.split(pattern_three_two,string)
# print(ret_three_two)  ##['jkh', '98.023', 'khj', '12', 'jhh', '64.5', 'jjk', '2', 'jhk', '6', 'k']
# 针对第二种对整个正则加()分组括号,并取消内部分组优先级的情况,则会按照我们实际整个正则匹配情况进行切割,并保留符合整个正则匹配内容的内容

# 3、re.search()方法分组的问题

# pattern_one = r'<(\w+)>(\w+)<(/\w+)>'
# string = '<h1>我是一个h1标签中的内容</h1>'
# ret = re.search(pattern_one,string)
# print(ret.group(0)) ## result = <h1>我是一个h1标签中的内容</h1>  group([0]) 保存整个正则表达式匹配的内容
# print(ret.group(1)) ## result = h1   从group(1)开始，按照自左向右的顺序，保存进行了分组的内容
# print(ret.group(2)) ## result = 我是一个h1标签中的内容
# print(ret.group(3)) ## result = /h1

# 4、re.match()方法分组的问题   除了match方法需要从开头开始强制匹配外，其他都和search方法一一致

# pattern_one = r'(\d+)(\.\d+)*'
# string = '98.023khj12jhh64.5jjk2jhk6k'
# ret = re.match(pattern_one,string)
# print(ret)
# if ret:
# 	print(ret.group(0)) ##result = 98.023
# 	print(ret.group(1)) ##result = 98
# 	print(ret.group(2)) ##result = 023


# ***********************************************************************
# 三、python中regular expression中"()"分组命名的使用问题,在分组符号内部的开头加上"?p<分组名称>"为分组命名

# 1、分组命名
# pattern_one = r'<(?P<first_lab>\w+)>(?P<content>\w+)<(?P<last_lab>/\w+)>'
# string = '<h1>我是一个h1标签中的内容</h1>'
# ret = re.search(pattern_one,string)
# print(ret.group(0)) ## result = <h1>我是一个h1标签中的内容</h1>  group([0]) 保存整个正则表达式匹配的内容
# print(ret.group('last_lab')) ## result = /h1   对分组进行命名后可以通过分组名来取值
# print(ret.group('first_lab')) ## result = h1
# print(ret.group('content')) ## result = 我是一个h1标签中的内容

# 2、向后引用 用来匹配相同的字符
# 通过分组命名向后引用  ?P<分组名>  ?P = 分组名 表示要找的内容和前面的分组一致
# pattern = r'\b(?P<same_world>\w+)\b\s+\b(?P=same_world)\b' ##匹配两个连续出现的相同的字符
# string = 'The pencil pencil is apple apple'
# ret = re.search(pattern,string)
# print(ret) ##result = <re.Match object; span=(4, 17), match='pencil pencil'>
# print(ret.group(0)) ##result = pencil pencil

# 通过分组编号进行向后引用 每一个()分组自左向右自动编号为\1、\2、....\n
# pattern = r'\b(?(?P<same_world>\w+)\b\s+\b\1\b' ##匹配两个连续出现的相同的字符  "\1"表示和第一个分组匹配内容相同
# string = 'The pencil pencil is apple apple'
# ret = re.search(pattern,string)
# print(ret) ##result = <re.Match object; span=(4, 17), match='pencil pencil'>
# print(ret.group(0)) ##result = pencil pencil)


# ***********************************************************************
# 四、python中regular expression操作方法中的可选flags参数
# re.I(IGNORECASE)忽略大小写，括号内是完整的写法
# re.M(MULTILINE)多行模式，改变^和$的行为
# re.S(DOTALL)点可以匹配任意字符，包括换行符
# re.L(LOCALE)做本地化识别的匹配，表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境，不推荐使用
# re.U(UNICODE) 使用\w \W \s \S \d \D使用取决于unicode定义的字符属性。在python3中默认使用该flag
# re.X(VERBOSE)冗长模式，该模式下pattern字符串可以是多行的，忽略空白字符，并可以添加注释
