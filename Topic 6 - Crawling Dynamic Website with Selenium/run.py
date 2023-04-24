from crawler import CharacterCrawler

if __name__ == "__main__":
    character_crawler = CharacterCrawler()
    character_crawler.crawl()
    character_crawler.export('data/myheroacademia.csv')