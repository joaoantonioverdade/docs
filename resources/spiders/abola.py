# -*- coding: utf-8 -*-
import os.path
import scrapy
from HTMLParser import HTMLParser
import sys

class euronewsptSpider(scrapy.Spider):
    name = "abola"
    allowed_domains = ["abola.pt"]
    start_urls = [
        "http://www.abola.pt/",
        "http://www.abola.pt/clubes/ver.aspx?t=3&id=589241",

    ]

    visit = []

    def parse(self, response):


        # data exists
        if hasattr(response, 'xpath'):

            # --------------------------------------------------------------
            # specific for each site
            title = response.xpath('//*[contains(concat(" ", normalize-space(@class), " "), " titulo arial-black")]')
            article = response.xpath('//div[@class="texto"]')

            if article and title:

                content = HTMLParser().unescape(title.extract()[0]) + "\n"
                content += HTMLParser().unescape(article.extract()[0])

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

                if "miragens" in url:
                    continue

                if url not in self.visit:
                    self.visit.append(url)

                    yield scrapy.Request(url, callback=self.parse)

