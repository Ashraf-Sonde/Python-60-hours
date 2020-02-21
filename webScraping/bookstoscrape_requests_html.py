from requests_html import HTMLSession
import urllib
import csv

session = HTMLSession()

urls = []
for i in range(1,51):
    urls.append(f'http://books.toscrape.com/catalogue/page-{i}.html')

csv_file = open('book_requests_html.csv', 'w')
csv_writer = csv.writer(csv_file, lineterminator='\n')

csv_writer.writerow(['Title', 'Price', 'ImageUrl'])

book_title = []
book_price = []
book_image_url = []
count = 1
for url in urls:
    source = session.get(url).html

    table = source.find('ol', first=True)
    blocks = table.find('li')

    for block in blocks:
        title = block.find('h3 a', first=True).attrs['title']
        book_title.append(title)

        image = block.find('div.image_container img', first=True)
        image_url = 'http://books.toscrape.com/'+image.attrs['src']
        book_image_url.append(image_url)

        urllib.request.urlretrieve(image_url, f"C:\\Users\\Hamdan\\Desktop\\webScraping\\images\\{title}.jpg")

        price = block.find('div.product_price p.price_color', first=True).text
        book_price.append(price)

        csv_writer.writerow([title, price, image_url])
        print(count, end='  ')
        count += 1

csv_file.close()

