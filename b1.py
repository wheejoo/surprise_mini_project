# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 01:45:44 2020

@author: wheejoo
"""
import pandas as pd

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.diningcode.com/profile.php?rid=PYk33Cv6jpwY")
soup = BeautifulSoup(html, "html.parser")


id = soup.select('.person-grade > .btxt > strong')
score = soup.select('.point-detail > span > .star')
menu = soup.find('div', {'class':'btxt'}).find('a')

ID = [i.text for i in id]
Score = [x.text for x in score]
Menu = menu.text

Rating = []
for k in range(1,len(ID)+1):
    Rating.append(Score[3*k])

sample = pd.DataFrame({
    'ID' : ID,
    'MENU' : Menu,
    'SCORE' : Rating})

excel_writer = pd.ExcelWriter('Sample.xlsx', engine='xlsxwriter')
sample.to_excel(excel_writer, index=False)
excel_writer.save()



    
