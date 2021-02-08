import urllib.request
import requests
import bs4
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
machine_learning = "https://medium.com/tag/machine-learning"
driver = webdriver.Chrome(
    "C:/Users/joyje/OneDrive/Desktop/MarbleAI/chromedriver.exe")
driver.get(machine_learning)
res = driver.execute_script("return document.documentElement.outerHTML")
driver.quit()
soup = BeautifulSoup(res, 'lxml')
work = []
for my_tag in soup.find_all(class_="ds-link ds-link--styleSubtle link--darken link--accent u-accentColor--textNormal"):
    work.append(my_tag.text)
para = []
for my_tag in soup.find_all(True, {'class': ['graf graf--h4 graf-after--h3 graf--trailing graf--subtitle', 'graf graf--p graf-after--figure', 'graf graf--p graf-after--h3 graf--trailing']}):
    para.append(my_tag.text)
title = []
for my_tag in soup.find_all(True, {'class': ['graf graf--h3 graf-after--figure graf--title', 'graf graf--h3 graf--leading graf--title', 'graf graf--h3 graf-after--figure graf--trailing graf--title']}):
    title.append(my_tag.text)
read = []
for my_tag in soup.find_all(class_="readingTime"):
    read.append(my_tag.get('title'))
upvotes = []
for my_tag in soup.find_all('span', {'class': 'u-textAlignCenter u-relative u-background js-actionMultirecommendCount u-marginLeft5'}):
    upvotes.append(my_tag.text)
date = []
for my_tag in soup.find_all('time'):
    date.append(my_tag.text)
name = []
for my_tag in soup.find_all(class_="ds-link ds-link--styleSubtle link link--darken link--accent u-accentColor--textNormal u-accentColor--textDarken"):
    name.append(my_tag.text)
content = []
alllink = []
for my_tag in soup.find_all(class_="postArticle postArticle--short js-postArticle js-trackedPost"):
    content.append(my_tag.text)
    for link in my_tag.find_all('a'):
        alllink.append(link.get('href'))
for i in range(0, len(content)):
    content[i] = content[i].replace(name[i], '')
    content[i] = content[i].replace(date[i], '')
    content[i] = content[i].replace(upvotes[i], '')
    content[i] = content[i].replace(title[i], '')
    content[i] = content[i].replace('…Read more…', '*')
    content[i] = content[i].replace('Read more…', '*')
    content[i] = content[i].replace('\xa0', ' ')
    content[i] = content[i].replace(' in ', '')
    for tag in work:
        content[i] = content[i].replace(tag, '')
    content[i] = content[i].split('*')
body = []
for i in range(0, len(content)):
    body.append(content[i][0])

res = []
for i in range(0, len(content)):
    if (len(content[i]) == 1):
        res.append('')
    else:
        res.append(content[i][1])

links = []
for my_tag in soup.find_all(class_="button button--smaller button--chromeless u-baseColor--buttonNormal"):
    links.append(my_tag.get('href'))

data1 = pd.DataFrame({'1.Theme': 'Machine Learning', '2.Name': name, '3.Title': title,
                      '4.Body': body, '5.Upvotes': upvotes, '6.Date': date, '7.Comments': res, '8.Link': links})
data1.to_csv('C:/Users/joyje/OneDrive/Desktop/medium1.csv', encoding='utf-8')
