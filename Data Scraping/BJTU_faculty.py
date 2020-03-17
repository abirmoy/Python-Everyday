# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 19:29:39 2019

@author: Abirmoy
"""

import requests
from bs4 import BeautifulSoup



def html_soup(url):
  r = requests.get(url)
  html_content = r.text
  html_soup = BeautifulSoup(html_content, 'html.parser')
  return html_soup

def email_soup(url, element, element_class):
  all_links = []
  n = []
  r = requests.get(url)
  html_content = r.text
  html_soup = BeautifulSoup(html_content, 'html.parser')
  email_soup = html_soup.find_all(element, {'class': element_class})
  
      
  # print(all_links)
  # print('\n',n)
  return email_soup




#overlayed_links.append(link['href'])
url = 'http://en.bjtu.edu.cn/Faculty_20161201183158288675/list_20161201183158288675/tmp_20161201183158288675/index.htm'
r = requests.get(url)
html_content = r.text
html_soup = BeautifulSoup(html_content, 'html.parser')

#link_soup = html_soup(url).find_all('a', {'class': 'red'})
# link_soup = link_soup(url, 'a', 'red')
# print(link_soup)
email_soup = html_soup.find_all('table', {'class': 'table-bordered'})
# tbody = email_soup.find('td')
# tbody = email_soup.find('tbody')
# print(type(tbody))
print(email_soup)
for email in email_soup:
  x = email.find_all('tr')
  for i in x:
    print(i.get_text(strip=True), '\n')




# trs = tbody.find_all('tr')