#!__*__coding:utf-8__*__
# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import os
import sys
import urllib.request
import json
import pandas as pd
import html
import get_main_content

client_id = "rMgnRYfDTJaJP067Dhqv"
client_secret = "oD33M7XoLJ"

def search_news_from_naver(keyword, start_idx): #맛집, 100
    global client_id, client_secret
    encText = urllib.parse.quote(keyword)
    url = "https://openapi.naver.com/v1/search/news?display=100&query=" + encText # json 결과
    url = url + "&start=" + str(start_idx)
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        result = response_body.decode('utf-8')
        return result
    else:
        print("Error Code:" + rescode)

def search_news_main(keyword):
    df = pd.DataFrame({}, columns=["title", "link", "originallink",
                                   "description", "pubDate"])
    for start_idx in range(1, 1000, 100):
        result = search_news_from_naver(keyword, start_idx)
        result2 = json.loads(result, encoding="utf-8")
        for one_item in result2["items"]:
            r2 = {
                "title": get_main_content.get_title(one_item["title"]),
                "link": html.unescape(one_item["link"]),
                "originallink": html.unescape(one_item["originallink"]),
                "description": one_item["description"],
                "pubDate": one_item["pubDate"],
            }
            try :
                x = get_main_content.get_main_content(html.unescape(one_item["originallink"]))
                r2["text"] = x;
            except:
            df = df.append(r2, ignore_index=True)
    output_filename = keyword + "_블로그검색결과.xlsx"
    df.to_excel(output_filename)

if __name__ == "__main__":
    search_news_main("부동산")