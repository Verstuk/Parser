import requests
from bs4 import BeautifulSoup as bs

headers = {'assept' : '*/*',
           'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36'}

# base_url = 'https://v1.spb.ru/nforum/viewtopic.php?f=4&t=5164&start=400'

def hh_parse(base_url, headers):
    session = requests.Session()
    request = session.get(base_url, headers = headers)
    if request.status_code == 200:
        soup = bs(request.content, 'html.parser')
        divs = soup.find_all('div', attrs={'class' : 'postbody'})
        l = (len(divs))
        titles = []
        conts = []
        for div in divs:
            title = div.find('p', attrs={'class':'author'}).text
            titles.append(title)
            content = div.find(attrs={'class':'content'}).text
            conts.append(content)
            # block = div.find('div', attrs='blockquote').text
            # print(block)
        i = 0
        for i in range(3):
            print(titles[l-i-1])
            print(conts[l-i-1])
            i += 1
    else:
        print('ERROR')

class color:
   YELLOW = '\033[93m'
   BOLD = '\033[1m'
   END = '\033[0m'

print('раздел "Вопросы и отзывы", тема "Общие вопросы"'.upper())
hh_parse('https://v1.spb.ru/nforum/viewtopic.php?f=2&t=5173&p=8236#p8236', headers)
print('')

print('раздел "Копицентр", тема "Копирование и печать"'.upper())
hh_parse('https://v1.spb.ru/nforum/viewtopic.php?f=4&t=5164&start=400', headers)
print('')

print('раздел "Копицентр", тема "Копирование и печать"'.upper())
hh_parse('https://v1.spb.ru/nforum/viewtopic.php?f=4&t=5164&start=400', headers)
print('')

print('раздел "Копицентр", тема "Визитки"'.upper())
hh_parse('https://v1.spb.ru/nforum/viewtopic.php?f=2&t=&p=6977#p6977', headers)
print('')

print('раздел "Копицентр", тема "Календари"'.upper())
hh_parse('https://v1.spb.ru/nforum/viewtopic.php?f=2&t=&p=7201#p7201', headers)
print('')

print('раздел "Копицентр", тема "Печать и брошюровка дипломов"'.upper())
hh_parse('https://v1.spb.ru/nforum/viewtopic.php?f=2&t=&p=7183#p7183', headers)
print('')

print('раздел "Копицентр", тема "Печать на футболках"'.upper())
hh_parse('https://v1.spb.ru/nforum/viewtopic.php?f=2&t=&p=7229#p7229', headers)
print('')

print('раздел "Копицентр", тема "Наклейки, печать и плоттерная резка"'.upper())
hh_parse('https://v1.spb.ru/nforum/viewtopic.php?f=2&t=&p=7142#p7142', headers)
print('')

print('раздел "Копицентр", тема "Сканирование документов, чертежей, плакатов"'.upper())
hh_parse('https://v1.spb.ru/nforum/viewtopic.php?f=2&t=&p=6889#p6889', headers)
print('')

print('раздел "Копицентр", тема "Брошюровка, ламинирование, наклейка на пенокартон, рамки"'.upper())
hh_parse('https://v1.spb.ru/nforum/viewtopic.php?f=2&t=&p=7289#p7289', headers)
print('')

print('раздел "Ваши отзывы", тема "Жалобы"'.upper())
hh_parse('https://v1.spb.ru/nforum/viewtopic.php?f=8&t=5187&p=7223#p7223', headers)
print('')

print ('раздел "Ваши отзывы", тема "Благодарности"'.upper())
hh_parse('https://v1.spb.ru/nforum/viewtopic.php?f=8&t=5186&p=7227#p7227', headers)
