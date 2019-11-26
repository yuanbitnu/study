# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.response.html import HtmlResponse


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://quotes.toscrape.com/page/1/']


    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                "author":quote.css('small.author::text').get(),
                "text":quote.css('span.text::text').get(),
                "tags":quote.css("a.tag::text").getall()
            }
        # response_url = response.urljoin('page')
        # print(response_url)        
##方式一、通过response.urljoin()方法构造绝对url并请求
        # next_page = response.css('li.next a::attr(href)').get()
        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page,callback= self.parse) #仅支持绝URL
##方式二、通过response.follow()方法接收相对url并请求
        # next_page = response.css('li.next a::attr(href)').get()
        # if next_page is not None:
        #     yield response.follow(next_page,callback = self.parse)#支持相对url
##方式三、response.follow()方法接收选择器(选择器必须提取必要属性)并请求
        # for href in response.css('li.next a::attr(href)'):
        #     yield response.follow(href,callback = self.parse)
##方式四、response.follow()方法接收一个属性的标签，自动使用其属性值构造url并请求
        for href in response.css('li.next a'):
            yield response.follow(href,callback = self.parse)
