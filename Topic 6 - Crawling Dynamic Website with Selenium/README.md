# Topic 6 - Data Crawling with Selenium

## What this repository do?

This is a demonstration of a simple web crawler to an [Anime wiki](https://myheroacademia.fandom.com/wiki/My_Hero_Academia_Wiki) (My Hero Academia). You will be able to scraped a group to websites for data analysis (if needed) or just keeping it as an achievement.

## How to run this repository?

**Step 1:** Go to the directory
```bash
cd "Topic 6 - Crawling Dynamic Website with Selenium"
```

**Step 2:** Install requirements
```bash
pip install -r requirements.txt
```

**Step 3:** Run the script
```bash
python run.py
```
*You can change any settings on `run.py`.*

## About Scrapy

Selenium is an open-source tool that automates web browsers.

Pros:
- Able to scrap dynamic sites

Cons:
- Limited data size.

## Struggle and Derived Tips during implementation

**1. XPATH**

Although Selenium supports many types of finding a web element or an hyperlink (can be found in [Locating Elements](https://selenium-python.readthedocs.io/locating-elements.html)), I have tried to use XPATH since we can use in both Scrapy and Selenium to extract the data.

More about XPATH can be learned and practiced [here](https://www.w3schools.com/xml/xpath_intro.asp)

**2. `find_element()` and `find_elements()`**

It is obvious that `s` goes as an plural indicator, but I put it here just in case people don't know how to get all elements satisfying the requirements instead of the first one only.

**3. Action Chains**

The repository did not work with clicking on web pages, which is an advantage of Selenium. It can be easily manipulated by just using an `ActionChains` and call some method `click()`, `click_and_hold()`, `drag_and_drop()` and put some elements as arguments.

Learn about it [here](https://www.geeksforgeeks.org/action-chains-in-selenium-python/)

## References:

- [Selenium Documentation](https://selenium-python.readthedocs.io/index.html).
- [Python Web-scraping with Selenium vs Scrapy vs BeautifulSoup by Thu Vu data analytics](https://www.youtube.com/watch?v=RuNolAh_4bU).