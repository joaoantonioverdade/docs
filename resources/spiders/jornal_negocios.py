# -*- coding: utf-8 -*-
import os.path
import scrapy
from HTMLParser import HTMLParser


class ObservadorSpider(scrapy.Spider):
    name = "jornal_negocios"
    allowed_domains = ["jornaldenegocios.pt"]
    start_urls = [
        "http://www.jornaldenegocios.pt",
    ]

    visit = []

    def parse(self, response):

        # self.parse_content(response)
        for href in response.css("a::attr('href')"):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_content)

    def parse_content(self, response):

        if hasattr(response, 'xpath'):

            title = response.xpath('//title')
            head = response.xpath('//*[contains(concat(" ",@class," "), " lead ")]')
            article = response.xpath('//*[contains(concat(" ",@class," "), " txt_artigo ")]')

            content = ""

            if title:
                content += title.extract()[0] + "\n"

            if head:
                content += head.extract()[0] + "\n"

            for line in article:
                content += HTMLParser().unescape(line.extract()) + "\n"

            filename = self.name + "/" + '-'.join(response.url.split("/")[3:]) + '.raw'

            if not os.path.isfile(filename):
                open(filename, "wb").write(content.encode('utf-8', 'ignore'))

        if hasattr(response, 'css'):
            for href in response.css("a::attr('href')"):
                url = response.urljoin(href.extract())

                if url not in self.visit:
                    self.visit.append(url)
                    yield scrapy.Request(url, callback=self.parse_content)
