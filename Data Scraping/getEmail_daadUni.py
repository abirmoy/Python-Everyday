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

def getEmail_daadUni(url):
  """
  URL: University Information In Daad website
  Returns: email of the University
  """
  # Getting the webpage, creating a Response object.
  response = requests.get(url)

  # Extracting the source code of the page.
  data = response.text

  # Passing the source code to BeautifulSoup to create a BeautifulSoup object for it.
  soup = BeautifulSoup(data, 'html.parser')
  
  ###
  # FOR SINGLE LINK IN A PAGE ENABLE BELLOW 2 LINES OF CODE, FOR ALL ENABLE COMMENTED PART
  tag = soup.find('a', {'class': 'btn btn-primary btn-block c-contact__link writeEmail'}) # Extracting the <a> tags into a list.
  print(tag.get('href')) # Extracting URLs from the attribute href in the <a> tags.


  # # Extracting all the <a> tags into a list.
  # tags = soup.find_all('a', {'class': 'btn btn-primary btn-block c-contact__link writeEmail'})

  # # Extracting URLs from the attribute href in the <a> tags.
  # for tag in tags:
  #     print(tag.get('href'))


urls = [
'https://www2.daad.de/deutschland/studienangebote/international-programmes/en/detail/7641/',
'https://www2.daad.de/deutschland/studienangebote/international-programmes/en/detail/7657/',
'https://www2.daad.de/deutschland/studienangebote/international-programmes/en/detail/4490/',
'https://www2.daad.de/deutschland/studienangebote/international-programmes/en/detail/7784/',
'https://www2.daad.de/deutschland/studienangebote/international-programmes/en/detail/4455/',
'https://www2.daad.de/deutschland/studienangebote/international-programmes/en/detail/5351/',
'https://www2.daad.de/deutschland/studienangebote/international-programmes/en/detail/4010/',
'https://www2.daad.de/deutschland/studienangebote/international-programmes/en/detail/4001/',
'https://www2.daad.de/deutschland/studienangebote/international-programmes/en/detail/4758/',
'https://www2.daad.de/deutschland/studienangebote/international-programmes/en/detail/4870/',
'https://www2.daad.de/deutschland/studienangebote/international-programmes/en/detail/7124/',
'https://www2.daad.de/deutschland/studienangebote/international-programmes/en/detail/3696/',
'https://www2.daad.de/deutschland/studienangebote/international-programmes/en/detail/4655/',
]

print('*'*50,"Printing e-mails", '*'*50, '\n'*5)
for url in urls:
  getEmail_daadUni(url)

print('\n'*5,'End')

