import scrapy

class RotlSpider(scrapy.Spider):
    name = 'rotl'
    start_urls = ['http://www.merlinmann.com/rotl-episodes/']

    def parse(self, resp):
        for url in resp.css('div.journal-archive-set ul li a::attr("href")').extract():
            yield scrapy.Request(resp.urljoin(url), self.parse_entry)

    def parse_entry(self, resp):
        link = resp.css('p.enclosureWrapper a::attr("href")').extract()[0]
        yield {'link': link,
               'category': 'Podcasts',
               'title': resp.css('h2.title a.journal-entry-navigation-current').xpath("text()").extract()[0],
               'guid': resp.url,
               'description': resp.css('div.body').extract()[0],
               'enclosure': link.replace('https://', 'http://'),
               'pubDate': resp.css('span.posted-on').xpath('text()').extract()[1],
            }
