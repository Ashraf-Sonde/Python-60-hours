import requests_html
from requests_html import HTMLSession,HTML,HTMLResponse

session = HTMLSession()
source = session.get('http://172.16.104.50/').html


source.render()

blocks = source.find('#test')
headlines = []
summaries = []

for block in blocks:
    headline = block.find('h2')[0]
    summary = block.find('p')[0]
    headlines.append(headline.text)
    summaries.append(summary.text)

print(headlines)
print(summaries)



footer = source.find('#footer')[0]

para = footer.find('p')
print(para[1].text)