from bs4 import BeautifulSoup
from requests_html import HTMLSession


session = HTMLSession()
source = session.get('https://www.zomato.com/mumbai/top-restaurants').html.html

soup = BeautifulSoup(source, 'lxml')


block = soup.find('div', class_='col-res-list collection_listings_container')
boxes = block.find_all('div', class_='col-s-8 col-l-1by3')
count = 1
for box in boxes:
    name = box.find('div', class_='res_title zblack bold nowrap').text.strip()
    location = box.find('div', class_='nowrap grey-text fontsize5 ttupper').text
    cuisine = box.find('div', class_='nowrap grey-text').text.strip()
    image = box.select('div.relative.top-res-box.entity-ads-snippet-track')[0].a['data-original']
    print(count)
    print()
    print(name)
    print(location)
    print(image)
    print()
    count += 1

