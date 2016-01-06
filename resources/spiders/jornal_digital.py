# -*- coding: utf-8 -*-
import os.path
import scrapy
from HTMLParser import HTMLParser


class ObservadorSpider(scrapy.Spider):
    name = "jornal_digital"
    allowed_domains = ["jornaldigital.com"]
    start_urls = [
        "http://www.jornaldigital.com",
    ]

    visit = []

    for n in range(18500, 47000):
        start_urls.append("http://www.jornaldigital.com/noticias.php?noticia=" + str(n))

    def parse(self, response):

        self.parse_content(response)
        # for href in response.css("a::attr('href')"):
        #     url = response.urljoin(href.extract())
        #     yield scrapy.Request(url, callback=self.parse_content)

    def parse_content(self, response):

        if hasattr(response, 'xpath'):
            title = response.xpath('//p[@class="titulo-artigo"]')
            head = response.xpath('//td[@class="bigheadline"]')
            article = response.xpath('//p[@align="justify"]')

            content = ""

            if title:
                content += title.extract()[0] + "\n"

            if head:
                content += head.extract()[0] + "\n"

            for line in article:
                content += HTMLParser().unescape(line.extract()) + "\n"

            filename = "jornal_digital/" + response.url.split("/")[-1] + '.raw'

            if not os.path.isfile(filename):
                open(filename, "wb").write(content.encode('utf-8', 'ignore'))

        # if hasattr(response, 'css'):
        #     for href in response.css("a::attr('href')"):
        #         url = response.urljoin(href.extract())

        #         if url not in self.visit:
        #             self.visit.append(url)
        #             yield scrapy.Request(url, callback=self.parse_content)
