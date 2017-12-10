import os
import sys
import urllib.request
import json
import pandas as pd
import html
import collections
from pytagcloud import create_tag_image, make_tags
from konlpy.tag import Kkma
from konlpy.utils import pprint
from collections import Counter
from bs4 import BeautifulSoup
import requests

def serach_blog(keyword, startIdx):

    client_id = "Yk2Ban58ISPqLXDlHOoi"
    client_secret = "4vPUnBdOH4"
    encText = urllib.parse.quote(keyword)
    url = "https://openapi.naver.com/v1/search/blog?display=100&query=" + encText + "start=" + str(startIdx) # json 결과
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        print(response_body.decode('utf-8'))
        return response_body
    else:
        print("Error Code:" + rescode)
        return ""

def savetoExcel(jsonResult) :
    data_dic = {
        "title":[],
        "bloggerlink": [],
        "bloggername": [],
        "description": [],
        "link": [],
        "postdate": [],
    }
    for one_item in jsonResult["items"]:
        data_dic.get("title").append(one_item["title"]);
        data_dic.get("link").append(html.unescape(one_item["link"]));
        data_dic.get("bloggerlink").append(html.unescape(one_item["bloggerlink"]));
        data_dic.get("bloggername").append(one_item["bloggername"]);
        data_dic.get("description").append(one_item["description"]);
        data_dic.get("postdate").append(one_item["postdate"]);

    df = pd.DataFrame(data_dic)
    print(df.head())
    df.to_excel("blog_data.xlsx")

def remove_empty_line(a):
    j = a.splitlines()
    x = []
    for i in j:
        if len(i.strip()) > 0:
            x.append(i)
    return "\r\n".join(x)

# 네이버 블로그 본문 가져오기
def get_main_content(url):
    response = requests.get(url)
    bs = BeautifulSoup(response.text, "lxml")
    c = bs.find(id="mainFrame")
    try :
        d = c["src"]
        e = "http://blog.naver.com" + d
        response2 = requests.get(e)
        bs = BeautifulSoup(response2.text, "lxml")
        bs = bs.find(id="postListBody")
        for rs in bs(["style", "script"]):
            rs.decompose()
        result = bs.get_text()
        result = remove_empty_line(result)
        return result
    except:
        return ""




## 파일의 description에서 단어 추출
blog_file_name = "C:\\git\\python_data__visual\\final_projet\\blog_data.xlsx"
def saveMainContent(file_name) :
    print(file_name)
    df = pd.read_excel(file_name)
    content_dic = { 'content_main' : []}
    for i in range(len(df)) :
        result = get_main_content(df.iloc[i].link)
        content_dic.get('content_main').append(result);
    result_df = pd.DataFrame(content_dic);
    result_df.to_excel("blog_main_content.xlsx")


        #
    # kkma = Kkma()
    # wordcount = Counter(kkma.nouns(des))
    # list(wordcount.items())

## 파일의 description에서 단어 추출
blog_main_content= "C:\\git\\python_data__visual\\final_projet\\blog_main_content.xlsx"
def makeCloudTag(file_name) :
    df = pd.read_excel(file_name);
    contents = list(df.content_main)
    result = ""
    for content in contents :
        result = result  + str(content) + " "

    kkma = Kkma()
    m = result.split("\r\n")
    nouns_list = []
    for a in m:
        nouns_list.append(kkma.nouns(a))

    nouns_list_s = []
    for i in nouns_list:
        for j in i:
            nouns_list_s.append(j)

    c = collections.Counter(nouns_list_s)
    x = c.most_common(100)
    d = make_tags(x, maxsize=100)
    create_tag_image(d, "star.jpg", size=(1000, 500), fontname='hangle')

makeCloudTag(blog_main_content)
#saveMainContent(blog_file_name)

# response = serach_blog("스타벅스", 1);
# result2 = json.loads(response , encoding="utf-8")
# savetoExcel(result2 )






