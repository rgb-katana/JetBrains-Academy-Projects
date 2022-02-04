import requests

import string

from bs4 import BeautifulSoup

import os


page_url = r"https://www.nature.com/nature/articles?sort=PubDate&year=2020&page="

page_number = int(input())
article_type_input = input()


def all_hylinks_page(url, page_num):
    current_url = url + str(page_num)
    r = requests.get(current_url)
    soup = BeautifulSoup(r.content, 'html.parser')
    hylinks = soup.find_all('article')
    return hylinks


def name_file(a_soup):
    head = a_soup.title.text.strip()
    file = head.translate(str.maketrans('', '', string.punctuation)).replace(" ", "_")
    return file


for page in range(1, page_number + 1):
    os.chdir(r'C:\Users\Komar\PycharmProjects\Web Scraper\Web Scraper\task')
    hyperlinks = all_hylinks_page(url=page_url, page_num=page_number)
    os.mkdir('Page_' + str(page))

    for link in hyperlinks:
        article_type = link.find('span', "c-meta__type").text
        if article_type == article_type_input:

            article_link = 'https://www.nature.com' + link.find('a').get('href')
            article_soup = BeautifulSoup(requests.get(article_link).content, 'html.parser')
            file_name = name_file(a_soup=article_soup)

            text = article_soup.find('div', attrs={"class": "c-article-body"}).text.strip().encode()
            os.chdir('Page_' + str(page))

            with open(f'{file_name}.txt', 'wb') as f:
                f.write(text)
                f.close()

print("All good.")
