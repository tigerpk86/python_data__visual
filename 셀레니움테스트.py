#!__*__coding:utf-8__*__

from selenium import webdriver
import time
from bs4 import BeautifulSoup
url = "http://entertain.naver.com/read?oid=001&aid=0009725056"
# "http://news.naver.com/main/read.nhn?m_view=1&includeAllCount=true&mode=LSD&mid=sec&sid1=100&oid=056&aid=0010525544"
browser = "D:\\chromedriver_win32\\chromedriver.exe"
DRIVER = webdriver.Chrome(browser)
DRIVER.get(url)
time.sleep(3)
DRIVER.find_element_by_class_name("u_cbox_in_view_comment").click()
time.sleep(1)
for i in range(50):
    try:
        DRIVER.find_element_by_class_name("u_cbox_more_wrap").click();
        time.sleep(1)
    except:
        break;

bs = BeautifulSoup(DRIVER.page_source, "lxml");
for rs in bs(["script", "style"]):
    rs.decompose()


#r.find_all("u_cbox_contents")
contents = bs.find_all("span", {"class":"u_cbox_contents"})
for i in contents:
    j = i.get_text()
    print(j)

r = bs.get_text();
open("result07.txt", "w").write(str(r));

DRIVER.quit()