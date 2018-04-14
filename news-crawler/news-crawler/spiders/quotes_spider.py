import scrapy
import time

WAITING_TIME = 5

def prefix_link(prefix: str, links: list):
    '''Add prefix to list of weblink.'''
    prefix_links = []
    for link in links:
        first_elem = link[:1]
        if first_elem is '/':
            prefix_links.append('https://' + prefix + link)
        else:
            prefix_links.append(link)
    return prefix_links

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    start_urls = [
        'https://www.spiegel.de/suche/index.html?suchbegriff=tafel+lebensmittel&quellenGroup=SP',
    ]

    def parse(self, response):
        links_article = response.css('div.search-teaser a::attr(href)').extract()
        links_article = list(set(links_article))
        print(prefix_link('spiegel.de', links_article))

        next_page = response.css('a.link-right::attr(href)').extract_first()
        if next_page is not None:
            time.sleep(WAITING_TIME)
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
