
import requests_html
from requests_html import HTMLSession,HTML,HTMLResponse

session = HTMLSession()
source = session.get('https://www.imdb.com/movies-in-theaters/?ref_=nv_mv_inth').html

boxes = source.find('div.list.detail.sub-list')[0]

blocks = boxes.find('.nm-title-overview-widget-layout')
for block in blocks:
    title = block.find('h4 a')[0].text
    print('TITLE : ' + title)
    runtime = block.find('p time')[0].text
    print('RUNTME : '+ runtime)
    genres = block.find('p')[0]
    genre = genres.find('span')
    print("GENRES : ", end=' ')
    for each_genre in genre:
        if(len(each_genre.text) > 2 ):
            print(each_genre.text)
            pass
    plot = block.find('div.outline')[0]
    print('PLOT :   \n' + plot.text)
    director = block.find('div.txt-block')[0]
    a = director.text.split('|')
    b = a[0].split('\n')
    a[0]  = b[1]
    print('LIST OF DIRECTORS')
    print(a)
    
    
    stars = block.find('div.txt-block')[1]
    try:
        a = stars.text.split(',')
        b = a[0].split('\n')
        a[0]  = b[1]
        print('LIST OF ACTORS')
        print(a)
        
    except Exception as identifier:

        print('NO STARS *********')
    print()
    print()        

