#!/usr/bin/env python
# coding: utf-8
import requests
import pandas as pd
from bs4 import BeautifulSoup
import lxml

url = "https://www.cututoronline.com/%E0%B8%84%E0%B8%A5%E0%B8%B1%E0%B8%87%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%AA%E0%B8%AD%E0%B8%9A/"
r= requests.get(url)
s = BeautifulSoup(r.text , 'lxml')
type(s)
d = s.find('ul' , {'id':'results'})
a_tags = d.find_all('a')

rows=[]
url_prefix = 'https://www.cututoronline.com'
for e in a_tags:
    try:
        img = e.find('img')
        name = img['alt']
        img_url = url_prefix + img['src']
        img_html = f'<img src="{src}" />'
        link = url_prefix + e['href']
        href_html = f'<a href="{link}">{name}</a>'
        rows.append((name , link , img_url , href_html , img_html))
    except:
        continue

df = pd.DataFrame(rows , columns=['name', 'link','img_url', 'href_html' , 'img_html' ])
df.to_csv('Pat1.csv' , index=False)

get_ipython().system('cat Pat1.csv')
Pat1 = pd.read_csv('Pat1.csv')
from IPython.display import HTML
HTML(df.to_html(escape=False))



