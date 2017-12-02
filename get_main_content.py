#!__*__coding:utf-8__*__

import requests
from bs4 import BeautifulSoup

def get_title(title):
    bs = BeautifulSoup(title, "lxml")
    return bs.get_text()

def get_main_content(url):
    response = requests.get(url)
    bs = BeautifulSoup(response.text, "lxml")
    c = bs.find(id="mainFrame")
    #c == None
    d = c["src"]
    e = "http://blog.naver.com" + d
    print(e)
    response2 = requests.get(e)
    bs = BeautifulSoup(response2.text, "lxml")
    bs = bs.find(id="postListBody")
    for rs in bs(["style", "script"]):
        rs.decompose()
    result = bs.get_text()
    return result

def remove_empty_line(a):
    j = a.splitlines()
    x = []
    for i in j:
        if len(i.strip()) > 0:
            x.append(i)
    return "\r\n".join(x)

result = get_main_content("http://blog.naver.com/09x43/221152682174")
result2 = remove_empty_line(result)
#print(result2)
fout = open("결과.txt", "w", encoding="utf-8")
fout.write(result2)
fout.close()