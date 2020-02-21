
import requests_html
from requests_html import HTMLSession,HTML,HTMLResponse

session = HTMLSession()
source = session.get('https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm').html
temp = source.html
print(temp)
# boxes = source.find('tbody')[0]
# match = boxes.find('tr')
# for box in match:
#     title = box.find('.titleColumn a')[0]
#     print('TITLE = ' + title.text)

#     rating = box.find('td.ratingColumn.imdbRating')[0]
#     print('RATING = ' + rating.text)


    
