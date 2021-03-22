from bs4 import BeautifulSoup as bs
import requests
flag = 0
animals = {}
wiki = 'https://ru.wikipedia.org/'
url ='https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pageuntil=%D0%90%D0%B7%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F+%D0%BF%D1%83%D0%B3%D0%BE%D0%BB%D0%BE%D0%B2%D0%BA%D0%B0#mw-pages'
while True:
    try:
        soup = bs(requests.get(url).text, 'html.parser')
        items = soup.find(id = 'mw-pages')
    except:
        break
    next_url = items.select("a")[flag]['href']
    b = items.select("div li a")
    if b[0]['title'][0]=='A':
        break
    for i in b:
        try:
            print(i['title'])
            animals[i['title'][0]] = animals[i['title'][0]]+1
        except KeyError:
            animals[i['title'][0]] = 1
    url = wiki+next_url
    flag = 1
del animals['A']
for key, value in animals.items():
    print(key,' - ', value)
