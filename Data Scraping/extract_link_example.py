# source: https://python.gotrained.com/beautifulsoup-extracting-urls/


from bs4 import BeautifulSoup
import requests

def getSoup(url):
  response = requests.get(url) # Getting the webpage, creating a Response object.
  data = response.text # Extracting the source code of the page.
  htmlsoup = BeautifulSoup(data, 'html.parser')
  return htmlsoup

def get_link(url, tag, tag_class='', suffix='', preffix=''):
  '''
    Input: URL, Tag, Tag Class(optional), Suffix(optional), Preffix(optional)
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

url = 'https://www.prothomalo.com/archive/2018-02-12?page=1'

# Getting the webpage, creating a Response object.
response = requests.get(url)

# Extracting the source code of the page.
data = response.text

# Passing the source code to BeautifulSoup to create a BeautifulSoup object for it.
soup = BeautifulSoup(data, 'html.parser')

# Extracting all the <a> tags into a list.
tags = soup.find_all('a', {'class': 'link_overlay'})

# Extracting URLs from the attribute href in the <a> tags.
for tag in tags:
    print(tag.get('href'))
