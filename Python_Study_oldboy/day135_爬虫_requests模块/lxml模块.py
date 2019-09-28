from lxml import etree
import requests

url = "https://changde.58.com/wuling/ershoufang/"
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'connection':'close',
}
respones_text = requests.get(url = url,headers=headers).text

element = etree.HTML(respones_text) # Element 对象
html_string = etree.tostring(element,encoding='utf-8') # 将Element对象转换为html文本

ul_li_lis = element.xpath('//ul[@class="house-list-wrap"]/child::li') # "//"表示搜索整个文档,不管该标签在什么位置,返回一个Element列表

for li in ul_li_lis:# xpath返回的都是list
    house_title = li.xpath('./div[@class = "list-info"]/h2/a/text()')[0] #.表示选取当前节点;"/text()"表示具体某个节点的文本内容;

    house_area_detail_lis = li.xpath('div[@class = "list-info"]/p[1]/span/text()')# 不写"."也是选取当前节点
    house_area_detail = ' '.join(house_area_detail_lis).strip()

    house_addr_detail_lis = li.xpath('div[@class = "list-info"]/p[2]/span/a/text()')
    house_addr_detail = ' '.join(house_addr_detail_lis).strip()

    house_price_sum_lis = li.xpath('div[@class = "price"]/p[1]//text()')# "//text()表示该节点下所有其他节点的文本内容"
    house_price_sum = " ".join(house_price_sum_lis).strip()

    house_unit_price = li.xpath('div[@class = "price"]/p[2]/text()')[0]

    print(house_title,house_area_detail,house_price_sum,house_unit_price,house_addr_detail)


