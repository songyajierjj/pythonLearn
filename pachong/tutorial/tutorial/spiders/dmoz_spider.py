# -*- coding: utf-8 -*-

from scrapy.spider import Spider   
from scrapy.selector import Selector
from tutorial.items import DmozItem
  
class DmozSpider(Spider):  
    name = "dmoz"  
    allowed_domains = ["dmoz.org"]  #搜索的域名范围，也就是爬虫的约束区域，规定爬虫只爬取这个域名下的网页
    start_urls = [  
        "http://www.milicaifu.com/" #"http://www.oschina.net/"  
    ]  
    def parse(self, response):  
        sel = Selector(response) 
        sites = sel.xpath('//ul[@class="QQ_line"]/li')  
        items = []
        for site in sites:  
        	item = DmozItem() 
        	item['title'] = site.xpath('a/text()').extract()
        	item['link'] = site.xpath('a/@href').extract()
        	item['desc'] = site.xpath('text()').extract()
        	items.append(item)
        return items