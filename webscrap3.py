from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import urllib.request
import requests
import bs4
from bs4 import BeautifulSoup
import csv
import pandas as pd
import time
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument(" — incognito")
machine_learning = "https://medium.com/tag/machine-learning"
driver = webdriver.Chrome(
    executable_path="C:/Users/joyje/OneDrive/Desktop/MarbleAI/chromedriver.exe", chrome_options=chromeOptions)
# driver.get("https://github.com/jeff10joy")
driver.get(machine_learning)
res = driver.execute_script("return document.documentElement.outerHTML")
driver.quit()
work = []
for my_tag in driver.find_elements_by_class_name("ds-link ds-link--styleSubtle link--darken link--accent u-accentColor--textNormal"):
    work.append(my_tag.text)
content = []
for c in driver.find_elements_by_xpath('/html/body/div/div/div[3]/article/div/section[2]/div/div'):
    para = []
    for i in c:
        para.append(i.text)
author = []
for a in driver.find_elements_by_xpath(
        '/html/body/div/div/div[3]/article/div/section[1]/div/div/div/div/div[1]/div[2]/div'):
    author.append(a.text)
timestamp = []
for t in driver.find_elements_by_xpath(
        '/html/body/div/div/div[3]/article/div/section[1]/div/div/div/div/div[1]/div[2]/span'):
    timestamp.append(t.text)

data = {'Tag': my_tag, 'Content': para,
        'Author': author, "Timestamp": timestamp, }
df = pd.DataFrame.from_dict(data, orient='index')
df.transpose()
df.to_csv('C:/Users/joyje/OneDrive/Desktop/MarbleAI/medium.csv', encoding='utf-8')
