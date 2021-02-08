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
article = "https://medium.com/@joy.jefferson10/yolo-you-look-only-once-algorithm-v2-5e2f18f7a83c"
driver = webdriver.Chrome(
    executable_path="C:/Users/joyje/OneDrive/Desktop/MarbleAI/chromedriver.exe", chrome_options=chromeOptions)
# driver.get("https://github.com/jeff10joy")
driver.get(article)
#res = driver.execute_script("return document.documentElement.outerHTML")
# driver.quit()
#work = []
# for my_tag in driver.find_elements_by_class_name("ds-link ds-link--styleSubtle link--darken link--accent u-accentColor--textNormal"):
# work.append(my_tag.text)
content = driver.find_elements_by_xpath(
    '/html/body/div/div/div[3]/article/div/section[2]/div/div')
para = []
for i in content:
    para.append(i.text)
author = driver.find_element_by_xpath(
    '/html/body/div/div/div[3]/article/div/section[1]/div/div/div/div/div[1]/div[2]/div').text
timestamp = driver.find_element_by_xpath(
    '/html/body/div/div/div[3]/article/div/section[1]/div/div/div/div/div[1]/div[2]/span').text
data = {'Tag': "computer vision", 'Author': author,
        "Timestamp": timestamp, 'Content': para}
df = pd.DataFrame.from_dict(data, orient='index')
df.transpose()
df.head(1)
df.to_csv('C:/Users/joyje/OneDrive/Desktop/MarbleAI/medium.csv', encoding='utf-8')
