from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

from notifier.files import BASE_DIR

class Scrapper:
    def __init__(self):
        self._get_ready_browser()

    
    def _get_ready_browser(self):
        try:
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            self._chrome_driver_path = BASE_DIR +"/driver/chromedriver"

            self._webdriver = webdriver.Chrome(
                executable_path=self._chrome_driver_path,
                options = chrome_options
                )
        except:
            print("Driver not found!")

    
    def get_news_headline(self):
        self._url = "https://www.prothomalo.com/"
        wait = WebDriverWait(self._webdriver, 10)
        self._webdriver.get(self._url)
        corona_div = self._webdriver.find_element_by_class_name("h-corona")
        marquee = corona_div.find_element_by_tag_name("marquee")
        spans = marquee.find_elements_by_tag_name("span")
        for span in spans:
            print(span.text)
        
        self._webdriver.close()


obj = Scrapper()
obj.get_news_headline()
        