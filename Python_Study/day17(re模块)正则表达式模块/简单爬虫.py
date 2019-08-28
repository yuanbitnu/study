import requests
import re


def download_web_page(url: str) -> str:
    '''
        下载指定url的网页源码
    '''
    return requests.get(url).text


def parse_page(str):
    pattern = r'class="item mod ".*?class="">(?P<name>.*?)</a>.*?"dt">(?P<date>.*?)</li>.*?"dt">(?P<class>.*?)</li>.*?"dt">(?P<countries>.*?)</li>.*?class="">(?P<nums>.*?)想看'
    iterator = re.finditer(pattern, str, flags=re.S)
    return iterator


def generator(iterator):
    for item in iterator:
        yield{
            '影片名': item.group('name'),
            '上映日期': item.group('date'),
            '类型': item.group('class'),
            '国家': item.group('countries'),
            '想看人数': item.group('nums'),
        }


def main():
    url = r'https://movie.douban.com/cinema/later/changde/'
    page_text = download_web_page(url)
    iterator = parse_page(page_text)
    generator_data = generator(iterator)
    print('__iter__' in dir(generator_data))
    with open('movie_information.txt', mode='a+', encoding='utf-8') as file_stream:
        for item in generator_data:
            file_stream.write(str(item))
            file_stream.flush()


def mains():
    pass


main()
