# -*- coding: utf-8 -*-
import scrapy


class AuthorSpider(scrapy.Spider):
    name = 'author'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        for href in response.css('small.author + a::attr(href)'):
            yield response.follow(href,callback = self.parse_author)
        
        for href in response.css('li.next a::attr(href)'):
            yield response.follow(href,callback = self.parse)
            
    
    def parse_author(self,response):
        yield {
            'author_name':response.css('h3.author-title::text').get(),
            'brithdate':response.css('span.author-born-date::text').get(),
            'author_description':response.css('div.author-description::text').get()
        }
