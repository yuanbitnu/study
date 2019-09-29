import requests
from lxml import etree
import urllib3

login_url = 'https://www.amazon.cn/ap/signin'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'connection':'close',
}
session = requests.Session()

page_text = session.post(login_url,headers = headers,data=data).text

userinfo_url ='https://www.amazon.cn/gp/css/homepage.html?ie=UTF8&ref_=nav_topnav_ya'
userinfo_page = session.get(url = userinfo_url,headers = headers)
code =  userinfo_page.status_code
print(code)
print('test')
