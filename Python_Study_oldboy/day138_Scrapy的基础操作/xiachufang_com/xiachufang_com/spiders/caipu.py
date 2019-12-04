# -*- coding: utf-8 -*-
import scrapy


class CaipuSpider(scrapy.Spider):
    name = 'caipu'
    allowed_domains = ['www.xiachufang.com']
    start_urls = ['http://www.xiachufang.com/']

    def parse(self, response):
        pass
