# -*- coding: utf-8 -*-
import os.path
import scrapy
from HTMLParser import HTMLParser


class euronewsptSpider(scrapy.Spider):
    name = "euronewspt"
    allowed_domains = ["pt.euronews.com"]
    start_urls = [
        "http://pt.euronews.com",
    ]

    visit = []

    def parse(self, response):

        # data exists
        if hasattr(response, 'xpath'):

            # --------------------------------------------------------------
            # specific for each site
            title = response.xpath('//title//text()')
            article = response.xpath('//div[@id="articleTranscript"]')

            if article and title:

                content = HTMLParser().unescape(title.extract()[0]) + "\n"
                content += HTMLParser().unescape(article.extract()[0])

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

                if "?" in url:
                    print("...skipping sorting...")
                    continue

                if url not in self.visit:
                    self.visit.append(url)

                    yield scrapy.Request(url, callback=self.parse)

