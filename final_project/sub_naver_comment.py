#!__*__coding:utf-8__*__
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from konlpy.tag import Kkma
kkma = Kkma()

DRIVER = None
browser = 'D:/chromedriver_win32/chromedriver.exe'


# 빈 줄만 찾아서 제거
def remove_empty_line(a):
    j = a.splitlines()
    x = []
    for i in j:
        if len(i.strip()) > 0:
            x.append(i)
    return "\r\n".join(x)


def get_naver_comment(url):
    global DRIVER, browser, kkma

    if DRIVER == None:
        DRIVER = webdriver.Chrome(browser)

    DRIVER.get(url)
    time.sleep(1)
    current_url = DRIVER.current_url
    bs = BeautifulSoup(DRIVER.page_source, "lxml")

    if current_url.find("news.naver.com") >= 0:
        cs = bs.find(id = "articleBodyContents")
    elif current_url.find("entertain.naver.com") >= 0:
        cs = bs.find(id = "articeBody")
    else:
        cs = bs

    full_content = remove_empty_line(cs.get_text())

    if url.find("naver.com") < 0:
        return ("NO FULL", "NO COMMENT", "NO COMMENT")

    try:
        DRIVER.find_element_by_class_name("u_cbox_in_view_comment").click()
    except:
        pass
    time.sleep(1)
    for i in range(50):
        try:
            DRIVER.find_element_by_class_name("u_cbox_page_more").click()
            time.sleep(1)
        except:
            break

    html = DRIVER.page_source
    bs = BeautifulSoup(html, "lxml")
    contents = bs.find_all("span", {"class":"u_cbox_contents"})
    result = []
    for i in contents:
        j = i.get_text()
        result.append(j)

    final_content = "\r\n".join(result)
    nouns = kkma.nouns(final_content)
    final_nouns = " ".join(nouns)

    return (full_content, final_content, final_nouns)

#url = "http://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=100&oid=001&aid=0009725083"
#result = get_naver_comment(url)
#print(result)
