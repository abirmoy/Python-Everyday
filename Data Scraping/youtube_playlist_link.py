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

def link_soup(url, element):
  '''THIS FUNCTION TAKES URL & ELEMENT TYPE OF THE PAGE AND RETRUNS LIST OF LINK IN THE PAGE'''
  all_links = []
  r = requests.get(url)
  html_content = r.text
  html_soup = BeautifulSoup(html_content, 'html.parser')
  link_soup = html_soup.find_all(element) 
  for link in link_soup:
    # FINDS ALL THE LINKS IN THE PAGE
    all_links.append(link['href'])

  return all_links


# LINK OF THE PAGE TO SCRAP
url = 'https://www.youtube.com/playlist?list=PLnbFC0ntxiqdpoWwMKCVh6BRwBePHaqQx'

link_soup = link_soup(url, 'a')
for link in link_soup:
  # IN ORDER TO AVOID UNNECESSARY LINKS AND ONLY PRINT THE LINK OF THE VIDEOS
  if '/watch' in link:
    print(f'ssyoutube.com/{link}')

# PRINT WHOLE PAGE
# print(html_soup(url).getText())