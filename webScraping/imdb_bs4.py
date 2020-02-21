import requests_html
from requests_html import HTMLSession,HTML,HTMLResponse
from bs4 import BeautifulSoup

titles = []
ratings = []
grossContent = []
weeks = []
session = HTMLSession()
response = session.get('https://www.imdb.com/chart/boxoffice/?ref_=nv_ch_cht').html
source = response.html
soup = BeautifulSoup(source, 'lxml')

box = soup.find('tbody')
rows = box.find_all('tr')
for row in rows:
    title = row.find('td', class_='titleColumn').text
    titles.append(title)
    rating = row.find('td', class_='ratingColumn').text.strip()
    ratings.append(rating)
    gross = row.find('span', class_='secondaryInfo').text
    grossContent.append(gross)
    week = row.find('td', class_='weeksColumn').text
    weeks.append(week)

for i in range(len(titles)):
    print(titles[i],weeks[i], ratings[i], grossContent[i])

