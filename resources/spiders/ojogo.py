# -*- coding: utf-8 -*-
import os.path
import scrapy
from HTMLParser import HTMLParser


class correio_manhaspider(scrapy.Spider):
    name = "ojogo"
    allowed_domains = ["ojogo.pt"]
    start_urls = [
        "http://www.ojogo.pt/",
    ]

    visit = []

    def parse(self, response):

        # data exists
        if hasattr(response, 'xpath'):

            # --------------------------------------------------------------
            # specific for each site
            title = response.xpath('//*[@id="NewsTitle"]')
            lead = response.xpath('//*[@id="NewsSummary"]')
            article = response.xpath('//div[@class="ArtText_1"]')

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
