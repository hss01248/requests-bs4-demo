import urllib

import requests
from bs4 import BeautifulSoup

headers = { "Accept":"text/html,application/xhtml+xml,application/xml;",
            "Accept-Encoding":"gzip",
            "Accept-Language":"zh-CN,zh;q=0.8",
            "Referer":"http://www.example.com/",
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"
            }


def getpic(url):
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    for link in soup.select('div.topic-figure > img '):
        src = link.get('src')
        name = src[src.rfind('/')+1 :] #逆序查找,找到最后一个/,截取后面的字符串作为文件名https://img3.doubanio.com/view/group_topic/large/public/p73727366.jpg
        urllib.request.urlretrieve(src, 'G:\\pythondemo\\' + name)  # 文件下载
        print(src+"--downloaded  name: "+'G:\\pythondemo\\' + name )



def getpage(page):
    r = requests.get('https://www.douban.com/group/duqi/discussion?start='+str(page*50)+'.html', headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    for link in soup.select('td.title > a'):
        url = link.get('href')
        print(url)
        getpic(url)


getpage(1)