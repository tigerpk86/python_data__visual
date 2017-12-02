#!__*__coding:utf-8__*__
from selenium import webdriver
browser = "C:\\Users\\505\Downloads\\chromedriver_win32\\chromedriver.exe"
url = "http://sports.news.naver.com/kfootball/news/read.nhn?oid=208&aid=0000001247"

driver = webdriver.Chrome(browser)
driver.get(url)
result = driver.page_source
print(result)