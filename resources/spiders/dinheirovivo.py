# -*- coding: utf-8 -*-
import os.path
import scrapy
from HTMLParser import HTMLParser


class dinheirovivospider(scrapy.Spider):
    name = "dinheirovivo"
    allowed_domains = ["dinheirovivo.pt"]
    start_urls = [
        "http://www.dinheirovivo.pt/",
    ]

    visit = []

    def parse(self, response):

        # data exists
        if hasattr(response, 'xpath'):

            # --------------------------------------------------------------
            # specific for each site
            title = response.xpath('//header[@class="article-header cf"]')
            lead = response.xpath('//div[@class="article-excerpt"]')
            article = response.xpath('//div[@class="entry-content cf"]')

            content = ""

            if title:
                content += HTMLParser().unescape(title.extract()[0]) + "\n"
            if lead:
                content += HTMLParser().unescape(lead.extract()[0]) + "\n"
            if article:
                for art in article:
                    content += HTMLParser().unescape(art.extract())

            if content != "":
                filename = self.name + "/"
                filename += response.url.split("/")[-2] + '.raw'
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
