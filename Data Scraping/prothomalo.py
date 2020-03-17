# -*- coding: utf-8 -*-
"""
Created on Tue Nov  21 20:14:08 2019
@author: Abirmoy
"""
import requests
from bs4 import BeautifulSoup
from datetime import date, timedelta
import os



overlayed_links = [] # TO STORE THE LINKS IN THE PAGES OF /ARCHIVE
start_date = date(2018, 2, 12)
end_date = date(2018, 2, 13)
delta = end_date - start_date
output_dir = './data-{}-{}'.format(start_date, end_date)
output_file_name = '{}-{}.json'.format(start_date,end_date)
all_articles = []

try:
    os.makedirs(output_dir)
except OSError:
    pass






try:
    for i in range(delta.days + 1):
        date = start_date + timedelta(days=i)
        page_number = 0
        while True:
            page_number = + 1
            # print(page_number)
            url = f'https://www.prothomalo.com/archive/{date}?page={page_number}'
            r= requests.get(url)
            html_content = r.text
            html_soup = BeautifulSoup(html_content, 'html.parser')



            archive_links = html_soup.find_all('a', {'class': 'link_overlay'})
            for link in archive_links:
                overlayed_links.append(link['href'])
                # print(link['href'])
                # print(type(link))
            # else:
            #     break # when overlayed_links is 0
            print(len(overlayed_links))
            while len(overlayed_links)!= 0:
                for link in overlayed_links:
                        one_article = []
                        # print(f'https://www.prothomalo.com/{link}')
                        url = f'https://www.prothomalo.com{link}'
                        r = requests.get(url)
                        html_content = r.text
                        html_soup = BeautifulSoup(html_content, 'html.parser')
                        headline = html_soup.find('h1', {'class': 'title mb10'})
                        # IT TURNS OUT SOME ARTICALE DOESNT HAVE REPORTER NAME MENTIONED
                        reporter_soup = html_soup.find('span', {'class': 'name'})
                        try:
                            reporter = reporter_soup.get_text()                            
                        except AttributeError:
                            reporter = 'Reporter name not given'
                        article = html_soup.find('div', {'itemprop': 'articleBody'})                
                        # STORING URL, DATE, HEADLINE, REPORTER AND THE ARTICLE TO THE LIST
                        one_article.append(date)
                        one_article.append(url)
                        # print(url) # TO CHECK THE 
                        one_article.append(headline.get_text())                   
                        one_article.append(reporter)    
                        one_article.append(article.get_text())                    
                        all_articles.append(one_article)
                        print('*'*80,f'\nHeadline:{headline.get_text()}\nReporter:{reporter}\nPublished Date:{date}\n')
                        # print(all_articles)
#        with open(output_dir+ '/' + output_file_name, 'w', encoding='utf8') as outfile:
#            json.dump(all_articles, outfile)
        
        text_file = open("Output.txt", "w", encoding='utf8')
        text_file.write(all_articles)
        text_file.close()
except requests.exceptions.ProxyError:
    print('I meet proxy error, please try another server')