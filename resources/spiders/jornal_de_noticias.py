# -*- coding: utf-8 -*-
import os.path
import sys
import scrapy
from HTMLParser import HTMLParser


class ObservadorSpider(scrapy.Spider):
    name = "jornalnoticias"
    allowed_domains = ["jn.pt"]
    start_urls = [
        "http://www.jn.pt",
    ]

    def parse(self, response):

        # self.parse_content(response)
        for href in response.css("a::attr('href')"):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_content)

    def parse_content(self, response):

        try:
            title = response.xpath('//title//text()')
            postTitle = response.xpath('//div[@class="postTitle"]//text()')
            article = response.xpath('//div[@class="articlePagination"]')


            if title and postTitle and article:

                content = HTMLParser().unescape(title.extract()[0])
                content += HTMLParser().unescape(postTitle.extract()[0])

                temp_article = article.extract()[0]
                temp_article = temp_article[:temp_article.find("<script")]

                content += temp_article

                filename = "jornal_noticias/" + response.url.split("/")[-1] + '.raw'

                print(response.url)

                if not os.path.isfile(filename):
                    open(filename, "wb").write(content.encode('utf-8', 'ignore'))

            for href in response.css("a::attr('href')"):
                url = response.urljoin(href.extract())
                yield scrapy.Request(url, callback=self.parse_content)

        except:
            print("Erro parse...", sys.exc_info()[0])
