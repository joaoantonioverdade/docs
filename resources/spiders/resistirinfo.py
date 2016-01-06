# -*- coding: utf-8 -*-
import os.path
import scrapy
from HTMLParser import HTMLParser

class resistirInfoSpider(scrapy.Spider):
    name = "resistirinfo"
    allowed_domains = ["resistir.info"]
    start_urls = [
        "http://resistir.info/",
    ]

    visit = []

    def parse(self, response):

        # data exists
        if hasattr(response, 'xpath'):

            # --------------------------------------------------------------
            # specific for each site
            bulk = response.xpath('//body')

            content = ""

            if bulk:
                content = HTMLParser().unescape(bulk.extract()[0]) + "\n"

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

