# -*- coding: utf-8 -*-

import scrapy
import io
from HTMLParser import HTMLParser


class ObservadorSpider(scrapy.Spider):
    name = "observador"
    allowed_domains = ["observador.pt"]
    start_urls = [
        "http://observador.pt/",
        # "http://observador.pt/2015/11/10/pcp/",
        # "http://observador.pt/opiniao/acabou-a-austeridade-reformados-vao-ter-aumento-de-18-euros/",

    ]
    def parse(self, response):
        for href in response.css("a::attr('href')"):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_content)

    def parse_content(self, response):

        content = None

        for sel in response.xpath('//title'):
            title = HTMLParser().unescape(sel.xpath('text()').extract()[0])
            # print "#Title:", HTMLParser().unescape(title[0])
            t = sel.xpath('text()').extract()[0]

        for sel in response.xpath('//*[contains(concat(" ", normalize-space(@class), " "), " content ")]'):
            content = sel.xpath('*').extract()
            # print HTMLParser().unescape(''.join(content))

        filename = "output/" + response.url.split("/")[-2] + '.raw'

        print(response.url)
        page = title + "\n"

        if content:
            for cont in content:

                if "<script " not in cont:
                    page += cont + "\n"

        open(filename, "wb").write(page.encode('utf-8', 'ignore'))

        for href in response.css("a::attr('href')"):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_content)

