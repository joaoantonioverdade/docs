# -*- coding: utf-8 -*-
import os.path
import sys
import scrapy
from HTMLParser import HTMLParser


class ObservadorSpider(scrapy.Spider):
    name = "ocasiao"
    allowed_domains = ["ocasiao.pt"]
    start_urls = [
        "http://www.ocasiao.pt/imocasiao/lousada-locais-comerciais-loja-c-27m2-no-cent-comerc-edinor-lousada-30-min-do-porto",
        # "http://www.ocasiao.pt",
        # "http://www.ocasiao.pt/autocasiao",
        # "http://www.ocasiao.pt/imocasiao",
        # "http://www.ocasiao.pt/emprego",
        # "http://www.ocasiao.pt/diversos",
        # "http://www.ocasiao.pt/prestacao-de-servicos",
        # "http://www.ocasiao.pt/lar-e-jardim",
        # "http://www.ocasiao.pt/tecnologia",
        # "http://www.ocasiao.pt/construcao-industria-e-comercio",
        # "http://www.ocasiao.pt/moda",
        # "http://www.ocasiao.pt/desporto",
        # "http://www.ocasiao.pt/animais",

    ]

    visit = []

    def parse(self, response):

        # self.parse_content(response)
        for href in response.css("a::attr('href')"):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_content)

    def parse_content(self, response):

        if hasattr(response, 'xpath'):
            article = response.xpath('//div[@id="description"]')
            if article:

                temp_article = article.extract()[0]
                temp_article = temp_article[:temp_article.find("<script")]

                content = temp_article

                filename = "ocasiao/" + response.url.split("/")[-2] + "_" + response.url.split("/")[-1] + '.raw'

                if not os.path.isfile(filename):
                    open(filename, "wb").write(content.encode('utf-8', 'ignore'))

        if hasattr(response, 'css'):
            for href in response.css("a::attr('href')"):
                url = response.urljoin(href.extract())

                # if "solrsort" in url:
                #     print("...skipping solsort...")
                #     continue

                if "?" in url and "page=" not in url:
                    print("...skipping sorting...")
                    continue

                if url not in self.visit:
                    self.visit.append(url)
                    yield scrapy.Request(url, callback=self.parse_content)

