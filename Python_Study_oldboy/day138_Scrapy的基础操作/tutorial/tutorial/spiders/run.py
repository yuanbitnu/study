from scrapy.cmdline import execute
import sys
import os
#获取当前脚本路径
dirpath = os.path.dirname(os.path.abspath(__file__))
print(dirpath)
#添加环境变量
sys.path.append(dirpath)
#启动爬虫,第三个参数为爬虫Name
#execute(['scrapy','crawl','quotes','-o','quotes.json']) ##将内容写入json文件中
#execute(['scrapy','crawl','author','-o','author_description.jl'])#将内容写JsonLines中
execute(['scrapy','crawl','quotes_with_args','-o','quotes_with_args.jl','-a','tag=books'])#带参数的scrapy命令 使用参数拼接特定的url
