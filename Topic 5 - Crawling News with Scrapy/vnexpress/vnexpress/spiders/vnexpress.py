import os
import time
import scrapy
import pandas as pd

from datetime import datetime


class VnExpressSpider(scrapy.Spider):
    name = 'vnexpress'
    start_urls = [
        'https://vnexpress.net/thoi-su/chinh-tri',
        'https://vnexpress.net/thoi-su/dan-sinh',
        'https://vnexpress.net/thoi-su/lao-dong-viec-lam',
        'https://vnexpress.net/thoi-su/giao-thong',
        'https://vnexpress.net/thoi-su/mekong',
        'https://vnexpress.net/thoi-su/quy-hy-vong',
        'https://vnexpress.net/the-gioi/tu-lieu',
        'https://vnexpress.net/the-gioi/phan-tich',
        'https://vnexpress.net/the-gioi/nguoi-viet-5-chau',
        'https://vnexpress.net/the-gioi/cuoc-song-do-day',
        'https://vnexpress.net/the-gioi/quan-su',
        'https://vnexpress.net/kinh-doanh/quoc-te',
        'https://vnexpress.net/kinh-doanh/doanh-nghiep',
        'https://vnexpress.net/kinh-doanh/chung-khoan',
        'https://vnexpress.net/kinh-doanh/bat-dong-san',
        'https://vnexpress.net/kinh-doanh/ebank',
        'https://vnexpress.net/kinh-doanh/vi-mo',
        'https://vnexpress.net/kinh-doanh/bao-hiem',
        'https://vnexpress.net/kinh-doanh/hang-hoa',
        'https://vnexpress.net/khoa-hoc/khoa-hoc-trong-nuoc',
        'https://vnexpress.net/khoa-hoc/tin-tuc',
        'https://vnexpress.net/khoa-hoc/phat-minh',
        'https://vnexpress.net/khoa-hoc/ung-dung',
        'https://vnexpress.net/khoa-hoc/the-gioi-tu-nhien',
        'https://vnexpress.net/khoa-hoc/thuong-thuc',
        'https://vnexpress.net/giai-tri/gioi-sao',
        'https://vnexpress.net/giai-tri/phim',
        'https://vnexpress.net/giai-tri/nhac',
        'https://vnexpress.net/giai-tri/thoi-trang',
        'https://vnexpress.net/giai-tri/lam-dep',
        'https://vnexpress.net/giai-tri/sach',
        'https://vnexpress.net/giai-tri/san-khau-my-thuat',
        'https://vnexpress.net/bong-da',
        'https://vnexpress.net/the-thao/marathon',
        'https://vnexpress.net/the-thao/tennis',
        'https://vnexpress.net/the-thao/bundesliga',
        'https://vnexpress.net/the-thao/cac-mon-khac'
    ]

    def parse(self, response):
        # Retrieve news category
        url_splited = response.url.split('/')       # Example: https://vnexpress.net/thoi-su/chinh-tri
        
        large_category = url_splited[-2]                                # Example: thoi-su
        large_category = large_category.replace('-', ' ').title()       # Example: Thoi Su

        small_category = url_splited[-1]                                # Example: chinh-tri
        small_category = small_category.replace('-', ' ').title()       # Example: Chinh Tri

        # Process the articles
        articles = response.css('article')
        for article in articles:
            title = article.css('h2.title-news').css('a::text').get()
            if title is not None:
                description = article.css('p.description').css('a::text').get()
                full_news_url = article.css('a::attr(href)').get()
                yield scrapy.Request(
                    full_news_url,
                    callback=self.parse_news_content,
                    cb_kwargs=dict(returned_dict={
                        'Title': title.replace('\n', ''),
                        'Description': description,
                        'Crawled Time': datetime.now(),
                        'Category': large_category,
                        'Sub-category': small_category,
                        'Source': 'vnexpress.net'
                    })
                )
        
        # # Combine it into a DataFrame
        # news_df = pd.DataFrame(news_object_lst)

        # # Save it to a file
        # filepath = 'news/news.csv'
        # if os.path.exists(filepath):
        #     existing_news_df = pd.read_csv(filepath, parse_dates=['Crawled Time'])
        #     news_df = pd.concat([existing_news_df, news_df], ignore_index=True)
        #     # Drop duplicates titles
        #     news_df.drop_duplicates(subset=['Title'], keep='first')
        # news_df.to_csv(filepath, index=False, encoding='utf-8')

    def parse_news_content(self, response, returned_dict):
        content = response.css('p.Normal::text').getall()
        # Remove duplicate content in list
        content = list(dict.fromkeys(content))
        content = ' '.join(content)
        
        returned_dict['Content'] = content
        yield returned_dict