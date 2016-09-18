# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 13:55:01 2016

@author: Allen
"""

from scrapy.spider import Spider  
      
class DmozSpider(Spider):  
    name = "dmoz"  
    allowed_domains = ["dmoz.org"]  
    start_urls = [  
            "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",  
            "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"  
            ]

    def parse(self,response):
        filename=response.url.split("/")[-2]
        open(filename, 'wb').write(response.body)
            
  