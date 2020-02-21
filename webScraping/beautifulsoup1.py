import requests_html
from requests_html import HTMLSession,HTML,HTMLResponse
from bs4 import BeautifulSoup

urls = []
for i in range(1,51):
    urls.append(f'http://books.toscrape.com/catalogue/page-{i}.html')

count = 1
for url in urls:
    session = HTMLSession()
    response = session.get(url).html
    source = response.html

    soup = BeautifulSoup(source, 'lxml')
    
    box = soup.find('ol')
    book_title = []
    book_price = []
    book_image = []

    elements = box.find_all('li')

    for element in elements:
        title = element.select('h3 a')[0]['title']
        book_title.append(title)
        price = element.find('p', class_='price_color').text
        book_price.append(price)
        image = element.find('img')['src']
        image_url = 'http://books.toscrape.com/' + image
        book_image.append(image_url)
        print(count, end='  ')
        count = count + 1

    
