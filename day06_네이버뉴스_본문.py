#!__*__coding:utf-8__*__

import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_title(title):
    bs = BeautifulSoup(title, "lxml")
    return bs.get_text()

def get_main_content(url):
    response2 = requests.get(url)
    bs = BeautifulSoup(response2.text, "lxml")
    bs = bs.find(id="article_content")
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

df = pd.read_excel("부동산_블로그검색결과.xlsx")
print(df)
for i in range(len(df)) :
    result = get_main_content("http://www.fnnews.com/news/201712021421177779")
    result2 = remove_empty_line(result)

#print(result2)
fout = open("결과.txt", "w", encoding="utf-8")
fout.write(result2)
fout.close()