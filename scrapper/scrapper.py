#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from notifier.files import BASE_DIR
import os, time

class Scrapper:
    def __init__(self):
        self._chrome_driver_path, self._webdriver = "", None
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
        print(BASE_DIR)
        self._url = "https://service.prothomalo.com/commentary/marquee/"
        wait = WebDriverWait(self._webdriver, 10)
        self._webdriver.get(self._url)
        time.sleep(5)
        # wait.until(presence_of_element_located((By.CSS_SELECTOR, ".h-corona")))
        marquees = self._webdriver.find_elements_by_tag_name("marquee")
        # print(marquee)
        # marquee = corona_div.find_element_by_tag_name("marquee")
        # spans = marquee[0].find_elements_by_tag_name("span")
        # for marquee in marquees[0]:
        #     print(marquee.text)
        
        self._webdriver.close()

        