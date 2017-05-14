import win32api

import pyautogui
import time

import requests
from bs4 import BeautifulSoup
from pywinauto.application import Application
import win32clipboard as wincb
import win32con


app = Application(backend="uia").start('C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe "https://www.baidu.com"')
#screenWidth, screenHeight = pyautogui.size()
#currentMouseX, currentMouseY = pyautogui.position()
time.sleep(8)
rightClickFirst = 20
itemWidth = 260
itemHeight = 220

#pyautogui.moveTo(1782, 672)#打开具体类别
print("clicked----")

def setNewTagForground():
    time.sleep(1)
    pyautogui.moveTo(296, 11)  # 将新打开的标签设置为当前标签
    pyautogui.click()


def openNewTag(x, y):
    pyautogui.rightClick(x, y)
    pyautogui.moveTo(x+rightClickFirst, y+rightClickFirst) #点击右键第一条,打开新的标签
    pyautogui.click()


def clickDownload():
    time.sleep(10)
    pyautogui.moveTo(1030, 900)
    pyautogui.click()



def click720p(x,y):
    time.sleep(2)

    # x, y = pyautogui.locateCenterOnScreen('F:/720p.jpg')
    # print(x,y)
    #
    # im = pyautogui.screenshot(region=(338, 921, 1294, 978))
    # button7location = pyautogui.locateOnScreen('f:\\720p.jpg')
    #
    # button7x, button7y = pyautogui.center(button7location)
    pyautogui.rightClick(x, y)
    pyautogui.hotkey('shift', 'e')  # 全选
    # pyautogui.rightClick(1004, 953) # 有1080p时,点击迅雷下载
    #pyautogui.moveTo(x+20, 1109)# 只有720p时点击迅雷下载

    #pyautogui.click()


def closeXunleiPanel():
    time.sleep(4)
    pyautogui.moveTo(1789, 376)
    pyautogui.click()

def nextitem():
    time.sleep(2)
    pyautogui.moveTo(859, 179)
    pyautogui.click()
    clickDownload()
    click720p(775, 960)
    saveUrl()
    click720p(1032, 958)
    saveUrl()




def copyurl():
    pyautogui.moveTo(581, 41)
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'a')  # 全选
    pyautogui.hotkey('ctrl', 'c')  # 复制

headers = { "Accept":"text/html,application/xhtml+xml,application/xml;",
            "Accept-Encoding":"gzip",
            "Accept-Language":"zh-CN,zh;q=0.8",
            "Referer":"http://www.example.com/",
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"
            }

def requestPage():

    wincb.OpenClipboard()
    url =  wincb.GetClipboardData(win32con.CF_TEXT)
    print(url)
    wincb.CloseClipboard()
    r = requests.get(url, headers=headers, verify=False)
    soup = BeautifulSoup(r.text, 'html.parser')
    for node in soup.select('a.downloadBtn greyButton '):
        href = node.get('href')
        print(href)
        if(href.find('720P') >0):
            print(href)

def saveUrl():
    wincb.OpenClipboard()
    url = wincb.GetClipboardData(win32con.CF_TEXT).decode('utf-8')
    print(url)
    wincb.CloseClipboard()
    with open('F:\\url.txt', 'a') as f:
        f.write(url+"\n")

openNewTag(732, 672)
setNewTagForground()
clickDownload()
#copyurl()
#requestPage()
click720p(775, 960)
saveUrl()
click720p(1032, 958)
saveUrl()
#closeXunleiPanel()

for i in range(1, 496):
    print(i)
    nextitem()





# app.UntitledNotepad.menu_select("帮助(&H)->关于记事本(&A)")
# app.AboutNotepad.确定.click()
# app.UntitledNotepad.Edit.type_keys("pywinauto Works!", with_spaces = True)
# app = Application(backend="uia").connect(path="explorer.exe", title="Program Files")
#
# app.ProgramFiles.set_focus()
# common_files = app.ProgramFiles.ItemsView.get_item('Common Files')
# common_files.right_click_input()
# app.ContextMenu.Properties.invoke()