
import csv
from bs4 import BeautifulSoup
import requests

def getSoup(url):
  response = requests.get(url) # Getting the webpage, creating a Response object.
  data = response.text # Extracting the source code of the page.
  htmlsoup = BeautifulSoup(data, 'html.parser')
  return htmlsoup

def get_link(url, tag, tag_class='', suffix='', preffix=''):
  '''
    Input: URL, Tag, Tag Class(optional)
    Output: List of links
  '''
  links = []
  response = requests.get(url) # Getting the webpage, creating a Response object.
  data = response.text # Extracting the source code of the page.
  htmlsoup = BeautifulSoup(data, 'html.parser')
  tags = htmlsoup.find_all(tag) if tag_class == '' else soup.find_all(tag, {'class': tag_class})

  # EXTRACTING LINKS IN A GIVEN PAGE
  for tag in tags:
    links.append(suffix + tag.get('href') + preffix)
  
  return links
  
def get_tag_text(htmlsoup, tag, tag_class=''):
  '''
    Input: URL, Tag, Tag Class(optional)
    Output: String
  '''
  tag_text = htmlsoup.find(tag).get_text() if tag_class == '' else soup.find(tag, {'class': tag_class}).get_text()
  return tag_text
  





url = 'https://see.tongji.edu.cn/szdw/dsmd/axkhf/jsjkxyjsxk.htm'

response = requests.get(url) # Getting the webpage, creating a Response object.
data = response.text # Extracting the source code of the page.
soup = BeautifulSoup(data, 'html.parser') # Passing the source code to BeautifulSoup to create a BeautifulSoup object for it.
tags = soup.find_all('a')# Extracting all the <a> tags into a list.


prof_links = []
# Fetching professor's Profile linke
for tag in tags:
  try:
    if '../../../' in tag.get('href'):
      prof_links.append(tag.get('href').replace('../../../', 'https://see.tongji.edu.cn/')) # .replace(old, new, count) 
  except TypeError:
    pass

