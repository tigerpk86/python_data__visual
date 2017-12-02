#!__*__coding:utf-8__*__

import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

def get_main_content():
    url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?targetDt=20171101&key=3e2abe22caed29f68de077821eba6c63"
    response = requests.get(url)
    a = json.loads(response.text, encoding="utf-8")
    df = pd.DataFrame({})
    for i in a["boxOfficeResult"]["dailyBoxOfficeList"]:
        result = {"영화명" : i["movieNm"], "매출액":i["salesAmt"]};
        df = df.append(result, ignore_index=True);
    df.to_excel("영화결과.xlsx")

# print(a)
get_main_content();
