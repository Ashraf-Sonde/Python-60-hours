import csv

import requests_html
from bs4 import BeautifulSoup
from requests_html import HTML, HTMLResponse, HTMLSession

csv_file = open('quoter.csv', 'w')
csv_writer = csv.writer(csv_file, lineterminator='\n')
csv_writer.writerow(['Title', 'Price', 'ImageUrl'])

urls = []
quote_list = []
author_list = []
tag_list = []
count = 1
for i in range(1,11):
    urls.append(f'http://quotes.toscrape.com/page/{i}/')
for url in urls:
    session = HTMLSession()
    response = session.get(url).html
    source = response.html
    soup = BeautifulSoup(source, 'lxml')

    elements = soup.find_all('div', class_='quote')
    for element in elements:
        quote = element.find('span', class_='text').text
        author = element.find('small').text
        try:
            tag_box = element.find('div', class_='tags')
            tags = tag_box.find_all('a', class_='tag')

            tags_text = []
            for tag in tags:
                tags_text.append(tag.text)

            quote_list.append(quote)
        except Exception as identifier:
            tags_text.append('NO TAGS HERE')
        author_list.append(author)
        tag_list.append(tags_text)
        csv_writer.writerow([quote, author, tags_text])

        print(count)
        count = count + 1
        print(quote)
        print(author)
        print(tags_text)
        print()
