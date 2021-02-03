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
# option.add_argument(" — incognito")
driver = webdriver.Chrome(
    executable_path="C:/Users/joyje/OneDrive/Desktop/MarbleAI/chromedriver.exe", chrome_options=chromeOptions)
# driver.get("https://github.com/jeff10joy")
driver.get(
    "https://medium.com/@joy.jefferson10/yolo-you-look-only-once-algorithm-v2-5e2f18f7a83c")
content = driver.find_elements_by_xpath(
    '/html/body/div[1]/div/div[3]/article/div/section[2]/div/div/p[2]')
para = []
for c in content:
    para.append(c.text)
data = {'Theme': 'Computer Vision', 'Content': para}
df = pd.DataFrame.from_dict(data, orient='index')
df.transpose()
df.to_csv('C:/Users/joyje/OneDrive/Desktop/medium.csv', encoding='utf-8')
