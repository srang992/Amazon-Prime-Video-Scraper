import scrapy
from scrapy.selector import Selector
from selenium import webdriver
import time


class AmazonPrimeSpider(scrapy.Spider):
    name = "AmazonPrimeBot"
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Windows NT 6.0; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0",
        "ROBOTSTXT_OBEY": False,
        "DOWNLOAD_DELAY": 10,
        "AUTOTHROTTLE_ENABLED": True,
        "AUTOTHROTTLE_START_DELAY": 10,
        "AUTOTHROTTLE_MAX_DELAY": 60,
        "AUTOTHROTTLE_TARGET_CONCURRENCY": 1.0,
        "AUTOTHROTTLE_DEBUG": False
    }

    def start_requests(self):
        url = "https://www.primevideo.com/search/ref=atv_cat_genre_actionadventure_quest?ie=UTF8&pageId=default&queryToken=eyJ0eXBlIjoicXVlcnkiLCJuYXYiOmZhbHNlLCJwdCI6ImJyb3dzZSIsInBpIjoiZGVmYXVsdCIsInNlYyI6ImNlbnRlciIsInN0eXBlIjoic2VhcmNoIiwicXJ5IjoiYnE9JTI4YW5kJTIwc29ydDolMjdmZWF0dXJlZC1yYW5rJTI3JTIwJTI4b3IlMjBhdl9wcmltYXJ5X2dlbnJlOiUyN2F2X2dlbnJlX2FjdGlvbiUyNyUyMGF2X3ByaW1hcnlfZ2VucmU6JTI3YXZfZ2VucmVfYWR2ZW50dXJlJTI3JTI5JTI5IiwidHh0IjoiQWN0aW9uIGFuZCBhZHZlbnR1cmUiLCJvZmZzZXQiOjAsIm5wc2kiOjMwfQ%3D%3D&phrase=Action%20and%20adventure&queryPageType=browse"

        yield scrapy.Request(url=url, callback=self.after_fetch)

    def after_fetch(self, response):
        driver = webdriver.Chrome("chromedriver.exe")
        driver.get(response.url)

        for _ in range(40):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(10)

        sel = Selector(text=driver.page_source)
        links = sel.xpath('//div[@class="av-hover-wrapper"]/div/div/div/div/div/div/a/@href').extract()
        for link in links:
            link = "https://www.primevideo.com" + link
            yield response.follow(url=link, callback=self.parse)

    def parse(self, response, **kwargs):
        movie_names = response.css('title::text').extract()[0].split(': ')[1]
        if not movie_names:
            movie_names = ""

        season = response.css('div.av-detail-section > div > span > span::text').extract()
        if not season:
            season = ""
        else:
            season = season[0]

        rating = response.css('div.av-detail-section > div > div > span.rjRAS3 > span::text').extract()
        if not rating:
            rating = ""
        else:
            rating = rating[0]

        year = response.css('div.av-detail-section > div > div > span.XqYSS8') \
            .xpath('./span[@data-automation-id="release-year-badge"]/text()').extract()
        if not year:
            year = ""
        else:
            year = year[0]

        age_rating = response.css('div.av-detail-section > div > div > span > span > span._2BZ5w7::text').extract()
        if not age_rating:
            age_rating = ""
        else:
            age_rating = age_rating[0]

        description = response.css('div.av-detail-section > div > div > div > div > div > div > div::text').extract()
        if not description:
            description = ""
        else:
            description = description[0]

        all_items = {'movie_title': movie_names, 'description': description, 'season': season,
                     'year': year, 'rating': rating, 'age_rating': age_rating}

        yield all_items
