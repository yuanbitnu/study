import requests
from bs4 import BeautifulSoup
import lxml

url = "http://www.xiachufang.com/category/"
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36', # 请求主体的身份标识,此处标识模拟浏览器进行访问
    "connection":'close', # TCP连接方式,keep_alive:保持连接;close:关闭连接
}
respones = requests.get(url = url,headers=headers) # 进行get请求,get请求的参数在url中.返回一个Response对象

bea_soup = BeautifulSoup(respones.text,'lxml')# 创建一个beautifulSoup对象,将解析器设置为lxml,需要解析的内容为response.text中的内容,text属性为文本,content为二进制

category_lis =[]

special_list = bea_soup.find_all(name = 'div',attrs={'class':'cates-list clearfix has-bottom-border pb20 mb20'})#找到所有div标签中,带有指定class属性的标签,返回的是一个element.Tag对象的列表
for i in range(1,len(special_list)):
    special_name = special_list[i].find('h3').string # 在special_list列表的Tag中继续找到第一个Tag"h3"标签,并取出该标签中的文本(如果Tag中还有其他标签,则string为None)
    special_sub_lis = special_list[i].find_all('a') #在special_list列表的Tag中继续找到所有的Tag"a"标签
    speclia_sub_name =[]
    for special_sub in special_sub_lis:  # 循环取出上面a标签中的文本
        speclia_sub_name.append(special_sub.string)
    category_lis.append({special_name:speclia_sub_name})


for item in category_lis:
    print(item)
    print('*'*100)

















