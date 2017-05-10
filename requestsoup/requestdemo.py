import urllib

import requests

r = requests.get('http://music.163.com/api/playlist/detail?id=3779629')#云音乐新歌榜
arr = r.json()['result']['tracks']

for i in range(10):
    name = str(1+1) + '' + arr[i]['name']+'.mp3'
    link = arr[i]['mp3Url']
    urllib.request.urlretrieve(link,'G:\\pythondemo\\'+name)#文件下载
    print(name+'下载完成')