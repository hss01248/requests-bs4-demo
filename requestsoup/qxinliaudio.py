from bs4 import BeautifulSoup
import requests


def getpage(page):
    r = requests.get('http://www.qxinli.com/index.php?s=/voice/index/index/page/'+str(page)+'.html')
    soup = BeautifulSoup(r.text, 'html.parser')

    for link in soup.find_all('source'):
        print(link.get('src'))

for i in [1, 2, 3]:
    getpage(i)