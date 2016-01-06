# -*- coding: utf-8 -*-
import os.path
import scrapy
from HTMLParser import HTMLParser
import sys

class visaoSpider(scrapy.Spider):
    name = "visao"
    allowed_domains = ["visao.sapo.pt"]
    start_urls = [
        "http://visao.sapo.pt/",
    ]

    visit = []

    def parse(self, response):


        # data exists
        if hasattr(response, 'xpath'):

            # --------------------------------------------------------------
            # specific for each site
            title = response.xpath('//h1[@class="title"]')
            lead = response.xpath('//h2[@class="lead"]')
            article = response.xpath('//div[@class="articleContent"]')

            content = ""

            if title:
                content += HTMLParser().unescape(title.extract()[0]) + "\n"
            if lead:
                content += HTMLParser().unescape(lead.extract()[0]) + "\n"
            if article:
                content += HTMLParser().unescape(article.extract()[0])

            if content != "":
                filename = self.name + "/"
                filename += response.url.split("/")[-1] + '.raw'
                # --------------------------------------------------------------

                if not os.path.isfile(filename):
                    content = content.encode('utf-8', 'ignore')
                    open(filename, "wb").write(content)

        # search for other links
        if hasattr(response, 'css'):
            for href in response.css("a::attr('href')"):
                url = response.urljoin(href.extract())

                if url not in self.visit:
                    self.visit.append(url)

                    yield scrapy.Request(url, callback=self.parse)

