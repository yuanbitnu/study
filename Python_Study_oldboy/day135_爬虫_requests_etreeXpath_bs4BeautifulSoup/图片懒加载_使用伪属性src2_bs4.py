import requests
from bs4 import BeautifulSoup
import lxml
import os 

url = 'http://sc.chinaz.com/tupian/caoyuantupian.html'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'connection':'close',
}

html_text = requests.get(url,headers=headers)
html_text.encoding = 'utf-8'
html_text = html_text.text
bs = BeautifulSoup(html_text,'lxml')
div = bs.find(name = 'div',attrs={'id':"container"})
img_lis = div.find_all(name = 'img')
for img in img_lis:
    file_name = img.get('alt')# 获取标签属性的值
    text = img.get_text() # 获取标签中的文本内容则使用 get_text()
    img_url = img.get('src2') # 该网站图片加载使用的是懒加载方式,img中使用的是伪属性src2
    img_data = requests.get(img_url,headers=headers).content

    if not os.path.exists("imgs"):
        os.mkdir('imgs')
        with open(r'imgs\%s.jpg'%file_name,mode='wb') as file_stream:
            file_stream.write(img_data)
    else:
        with open(r'imgs\%s.jpg'%file_name,mode='wb') as file_stream:
            file_stream.write(img_data)
print('下载完毕')