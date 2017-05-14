import asyncio
import urllib

import requests
from bs4 import BeautifulSoup

headers = { "Accept":"text/html,application/xhtml+xml,application/xml;",
            "Accept-Encoding":"gzip",
            "Accept-Language":"zh-CN,zh;q=0.8",
            "Referer":"https://www.pornpics.com/skirt",
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"
            }

@asyncio.coroutine
def download(src, name):
    urllib.request.urlretrieve(src, 'F:\\xxhubs\\' + name)  # 文件下载
    r =yield from asyncio.sleep(1)
# 获取EventLoop:
loop = asyncio.get_event_loop()


def getpic(url, title):
    r = requests.get(url, headers=headers, verify=False)
    soup = BeautifulSoup(r.text, 'html.parser')
    for link in soup.select('a.rel-link'):
        src = link.get('href')
        name = src[src.rfind('/')+1 :] #逆序查找,找到最后一个/,截取后面的字符串作为文件名https://img3.doubanio.com/view/group_topic/large/public/p73727366.jpg
        #urllib.request.urlretrieve(src, 'F:\\xxhub\\' + name)  # 文件下载
        loop.run_until_complete(download(src, name))
        print(src+"--downloaded  name: "+'F:\\xxhub\\' + name )



def getpage():
    r = requests.get('https://www.baidu.com', headers=headers, verify=False)
    soup = BeautifulSoup(r.text, 'html.parser')

    for link in soup.select('div.img videoPreviewBg > a'):
        href = 'https://www.pornhub.com' + link.get('href')
        title = link.get('data-title')

        print(href + "---" + title)
        getpic(href, title)


getpage()


# 执行coroutine

#loop.close()