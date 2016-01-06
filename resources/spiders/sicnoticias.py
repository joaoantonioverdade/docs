# -*- coding: utf-8 -*-
import os.path
import sys
import scrapy
from HTMLParser import HTMLParser


class ObservadorSpider(scrapy.Spider):
    name = "sicnoticias"
    allowed_domains = ["sicnoticias.sapo.pt"]
    start_urls = [
        "http://sicnoticias.sapo.pt",
    ]

    def parse(self, response):

        # self.parse_content(response)
        for href in response.css("a::attr('href')"):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_content)

    def parse_content(self, response):

        try:
            # More than one title per article... without distinction
            # skipping titles...
            # title = response.xpath('//div[@class="titleContainer"]')

            lead = response.xpath('//div[@class="leadContainer text"]')
            article = response.xpath('//div[@class="bodyContainer text"]')

            if lead and article:

                content = HTMLParser().unescape(lead.extract()[0]) + "\n"
                content += HTMLParser().unescape(article.extract()[0])

                filename = "sicnoticias/" + response.url.split("/")[-1] + '.raw'
                print(filename)

                if not os.path.isfile(filename):
                    open(filename, "wb").write(content.encode('utf-8', 'ignore'))

            for href in response.css("a::attr('href')"):
                url = response.urljoin(href.extract())
                yield scrapy.Request(url, callback=self.parse_content)

        except:
            print("Erro parse...", sys.exc_info()[0])
