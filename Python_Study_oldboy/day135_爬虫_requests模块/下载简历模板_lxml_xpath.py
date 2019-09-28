import requests
from lxml import etree
import random
import os

url = 'http://sc.chinaz.com/jianli/free.html'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'connection':'close',
}

html_response = requests.get(url = url,headers=headers)
html_response.encoding = 'utf-8' #网站编码和当前python环境编码不一致,需要统一编码
html_text = html_response.text
etr = etree.HTML(html_text) # 返回的是element对象

div_lis = etr.xpath('//div[@id = "container"]/child::div')

if not os.path.exists('files_cv'):
    os.mkdir('files_cv')

for div in div_lis:
    new_url = div.xpath('./p/a/@href')[0] #获取"a"标签的href属性
    file_name = div.xpath('./p/a/text()')[0] #获取"a"标签中的文本属性
    new_html = requests.get(new_url,headers=headers)
    new_html.encoding = 'utf-8' # 统一编码
    new_html_text = new_html.text
    etr_one = etree.HTML(new_html_text)
    down_url_lis = etr_one.xpath('//div[@id = "down"]//li/a/@href') # "//"不管是儿子还是孙子都找出来 "/"只找儿子
    choice_url = random.choice(down_url_lis)
    file_byte = requests.get(choice_url).content
    with open(r'files_cv\%s.rar'%file_name,mode='wb') as file_stream:
        file_stream.write(file_byte)

print('下载完成')







