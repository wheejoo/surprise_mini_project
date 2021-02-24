# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 12:57:31 2020

@author: wheejoo
"""

import pandas as pd
from urllib.request import urlopen
import urllib.parse
import requests
from bs4 import BeautifulSoup

base_html = urlopen("https://www.diningcode.com/list.php?query=%EA%B0%95%EB%82%A8")
soup = BeautifulSoup(base_html, "html.parser")

f_id = soup.find_all('a', {'class' : 'blink'})
F_ID = [y['href'] for y in f_id]
                                    
f = open('test3.txt', 'w')

for page in range(len(F_ID)):
    raw = requests.get('https://www.diningcode.com' + F_ID[page], headers={'User-Agent': 'Mozilla/5.0'})
    bsoup = BeautifulSoup(raw.content, "html.parser")
    
    id = bsoup.select('.person-grade > .btxt > strong')
    score = bsoup.select('.point-detail > span > .star')
    menu = bsoup.find('div', {'class':'btxt'}).find_all('a')

    ID = [i.text for i in id]
    Score = [x.text for x in score]
    Menu = [z.text for z in menu]
    
    for k in range(1,len(ID)+1):
        f.write("{0} {1} {2}\n".format(ID[k-1], (','.join(Menu)), Score[3*k]))
    
    f.write("\n")

f.close()