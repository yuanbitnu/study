str1 = 'hello,world'
print(f'获取字符串的长度 = {len(str1)}')

print(f'获得字符串手写字母大写的拷贝 = {str1.capitalize()}')

print('获得字符串变大写后的拷贝 = ',str1.upper())

print('使用find方法从字符串中查找子串所在的位置 = ',str1.find('or'))

print('使用find方法从字符串中查找子串所在位置时,如果子串不存在的情况 = ',str1.find('shit'))

print('使用index方法从字符串中查找子串所在的位置 = ',str1.index('or'))

# print('使用index方法从字符串中查找子串所在的位置,如果子串不存在的情况 = ',str1.index('shit')) #使用index时如果子串不存在则会引发异常
print('检查字符串是否以指定字符串开头 = ',str1.startswith("hel"))

print('检查字符串是否以指定字符串开头 = ',str1.startswith("Hel"))

print('检查字符串是否以指定字符串结尾 = ',str1.endswith("d"))

print('将字符串以指定的宽度居中,并在其两侧填充指定字符:',str1.center(20,'*'))

print('将字符串以指定宽度居右,并在左侧以指定字符填充:',str1.rjust(20,"*"))


str2 = 'abc123456'

print('从字符串中取出索引为2的字符 = ',str2[2])

#对字符串进行切片(从指定的开始索引到指定的结束索引,其范围是包前不包后)

print('对字符串进行切片: ',str2[0:2]) # ab 切出的index为 0-1

print('对字符串进行切片: ',str2[2:])  # c123456 可以省略结束索引,代表从指定的开始位置到最后并且包括最后  

print('对字符串进行切片: ',str2[:3])  # abc  可以省略开始索引,代表从首位切到指定的结束索引,其范围不包括最后索引

print('对字符串按照指定步长进行切片: ',str2[2::2]) # c246 省略了结束索引,切片的步长为2,代表从索引2开始到字符串最后,按照步长为2 进行切片

print('对字符串按照指定步长进行切片: ',str2[::2]) # ac246  省略了开始和结束索引,切片步长为2,代表对整个字符串按照步长为2 进行切片

print("对字符串按照步长为-1进行切片: ",str2[::-1]) #654321cba  省略了开始和结束索引,切片步长为-1,会将整个字符串反转,步长为-1时切片范围必须是整个字符串

print('对字符串进行切片: ',str2[-3:-1]) #45 index为-1 代表的是从字符串最后一位,-2代表倒数第二位  切片时[-3:-1]切片范围还是包前不包后,即从index为-3的开始到index为-1但不包括-1

str3 = '123'
str4 = 'abc'

print('检查字符串是否全由数字构成: ',str3.isdigit(),str3.isalpha())

print('检查字符串是否全由字母构成: ',str4.isdigit(),str4.isalpha())

print('如果一段字符串既有数字又有字母,则方法 isdigit() 和 isalpha() 都为False :',str2.isdigit() ,str2.isalpha())

print('检查一段字符串是否既有数字又有字母: ',str2.isalnum())

str5 = '   jackfrue@126.com  '

print('获得字符串修建左右两侧空格后的拷贝: ',str5.strip())