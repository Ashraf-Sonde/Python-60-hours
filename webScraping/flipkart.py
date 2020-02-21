# make sure you enable less secure apps permission in google settings
# just google "google less secure apps"


from requests_html import HTMLSession
from bs4 import BeautifulSoup
import smtplib
import webbrowser as wb

session = HTMLSession()
url = 'https://www.flipkart.com/oneplus-7t-glacier-blue-128-gb/p/itma74f3aece46b1?pid=MOBFKWSYWB5S37YV&lid=LSTMOBFKWSYWB5S37YVVOK0W3&marketplace=FLIPKART&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_0_6_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_0_6_na_na_na&fm=SEARCH&iid=12dca22d-b519-4fdf-a5dd-178b624ad7ef.MOBFKWSYWB5S37YV.SEARCH&ppt=sp&ppn=sp&ssid=pe1z583shs0000001582216955646&qH=14b5a22b29c5f381'

response = session.get(url)

source = response.html.html
soup = BeautifulSoup(source, 'lxml')

price = soup.find('div', class_='_1vC4OE _3qQ9m1')
final_price = int(price.text.replace(',', '')[1:])
name = soup.find('span', class_='_35KyD6').text
print(name, final_price)

if(final_price < 35000):
    print('AUKAT KE ANDAR')


    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('sender email here', 'password here')

    subject = 'ITS YOUR LUCKY DAY'
    body = f'Check your amazon account {url}'
    msg = f"Subject : {subject}\n\n{body}"
    server.sendmail(
        'sender email here',
        'receiver email here',
        msg 
    )

    print('done')
    # wb.open_new_tab(url)

    server.quit()
    
else:
    print('AUKAT KE BAHAR')
    

    