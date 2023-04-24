import pandas as pd

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class CharacterCrawler():
    
    def __init__(self, from_episode = 1, to_episode = 113):
        self.from_episode = from_episode
        self.to_episode = to_episode
        self.data = None
        
    def crawl(self):
        print("Crawling starts...")
        page_url = "https://myheroacademia.fandom.com/wiki/Story_Arcs"
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(page_url)
        
        # Get all episodes' links
        # We used a for loops instead of a list comprehension to avoid crawling an unexisting episode
        episode_links = []
        print("Getting all episode links...")
        for i in range(self.from_episode, self.to_episode + 1):
            try:
                ep = driver.find_element(By.XPATH, f"//a[@title='Episode {i}']")
                episode_links.append(ep.get_attribute('href'))
            except:
                print(f"Cannot find episode {i+1}. Skipping...")
                episode_links.append(None)
        
        appearance_lst = []
        for i, ep in enumerate(episode_links):
            print(f"Getting character in episode {i+1}...")
            if ep is None:
                continue
            try:
                driver.get(ep)
                lists_characters = driver.find_element(
                    By.XPATH,
                    "//span[starts-with(@id,'Character')]/parent::h2/following-sibling::div/ul"
                )
                characters = lists_characters.find_elements(By.XPATH, "./li")
                for c in characters:
                    text = c.text
                    splitted = text.split(' (')
                    if len(splitted) == 2:
                        appearance_lst.append([i + 1, splitted[0], splitted[1][:-1]])
                    else:
                        appearance_lst.append([i + 1, text, 'Direct'])
            except Exception as e:
                print(f"Cannot find characters in episode {i + 1}. Reason {e}")
            
        self.data = pd.DataFrame(appearance_lst, columns=['Episode', 'Character', 'Type of appearance'])
        print("Crawling completed!")
        
    def export(self, path):
        if self.data is None:
            print("Data does not exists, please perform a successful crawl!")
        else:
            self.data.to_csv(path, index=False)
            print("Exported successfully")