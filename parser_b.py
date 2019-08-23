import requests
from bs4 import BeautifulSoup as bs

headers = {'assept' : '*/*',
           'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36'}

base_url = 'https://v1.spb.ru/nforum/viewtopic.php?f=4&t=5164&start=400'

def hh_parse(base_url, headers):
    session = requests.Session()
    request = session.get(base_url, headers = headers)
    if request.status_code == 200:
        soup = bs(request.content, 'html.parser')
        divs = soup.find_all('div', attrs={'class' : 'postbody'})
        print(len(divs))
        for div in divs:
            title = div.find('p', attrs={'class':'author'}).text
            print(title)
            content = div.find(attrs={'class':'content'}).text
            print(content)
            # block = div.find('div', attrs='blockquote').text
            # print(block)
    else:
        print('ERROR')

hh_parse(base_url, headers)
