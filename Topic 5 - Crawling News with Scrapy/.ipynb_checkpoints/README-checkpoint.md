# Topic 5 - Data Crawling with Scrapy

## What this repository do?

This is a demonstration of a simple web crawler to one of the most-read Vietnamese news website. You will be able to scraped a group to websites for data analysis (if needed) or just keeping it as an achievement.

## How to run this repository?

**Step 1:** Go to the directory
```bash
cd "Topic 5 - Crawling News with Scrapy/vnexpress"
```

**Step 2:** Install requirements
```bash
pip install -r requirements.txt
```

**Step 3:** Run the spider by the following script
```bash
scrapy crawl vnexpress -t csv -o news/news.csv
```
*The `-t csv -o news/news.csv` is to save collected data into the `.csv` file.*

## About Scrapy

Scrapy is a complete web scraping framework, providing spiders for crawling through entire websites in a systematic way.

Pros:
- Fast
- Powerful
- Can handle large amount of data

Cons:
- Not beginner-friendly

## Struggle and Derived Tips during implementation

**1. The direct path to read before being dizzy**

Although the amount of code is large, most of them is automatically generated using `scrapy startproject <project_name>`. The place that you mostly work on is under `<project_name>/<project_name>/spiders`.

**2. Best Pratices for Crawl a website**

It is easier to:
- Firstly view the content of a website that scrapy can crawl by the command `scrapy view <url>` or create the first spider as in the [Scrapy tutorial](https://docs.scrapy.org/en/latest/intro/tutorial.html). There are some dynamic websites that requires you to crawl in a different way or different framework (e.g., Selenium).
- Practice extracting data with `scrapy shell <url>`, while opening your collected `.html` file in the previous step.
- Then finally paste your successful steps into your Spider's implementation.

**3. Aggregate data from several pages**

Although I can directly accessed a news and crawl all of them, I accidentally wanted to get some information from the parent page and add the content when accessing to the child page. The most straightforward way is seen in line 68.
```python
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
```

I just created a request to the child page to add content, and passed my dictionary obtained from extracting information from the parent page to the `callback` function. Scroll down the file to see the content of the callback function.

Note that we use `yield` instead of `return` to get a Generator.

## References:

- [Scrapy Tutorial](https://docs.scrapy.org/en/latest/intro/tutorial.html).
- [Python Web-scraping with Selenium vs Scrapy vs BeautifulSoup by Thu Vu data analytics](https://www.youtube.com/watch?v=RuNolAh_4bU).