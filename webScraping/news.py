from requests_html import HTMLSession
from bs4 import BeautifulSoup
import webbrowser as wb

url = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGRqTVhZU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen"
session = HTMLSession()

response = session.get(url)
print(response)
source = response.html.html
soup = BeautifulSoup(source, 'lxml')

box = soup.find('main', class_='HKt8rc CGNRMc')
count = 1
articles = box.find_all('h3', class_='ipQwMb ekueJc RD0gLb')
for article in articles:
    headline = article.text
    headline_link = "https://news.google.com/"+article.a.attrs['href']
    print(headline)
    print(headline_link, '\n\n')
    


