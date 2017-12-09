#!__*__coding:utf-8__*__

"""
프로그램 설치
pip install folium

여기서 한국 지도 JSON 파일 받을 수 있을 것
https://github.com/southkorea
https://github.com/southkorea/seoul-maps/tree/master/kostat/2013/json

seoul google 지도에 표기하기 위해서는 seoul.json 사용할 것
전국 google 지도에 표기하기 위해서는 skorea_municipalities_geo_simple.json 사용할 것

시도 표시는 skorea_provinces_geo_simple.json
이 파일은 수정되어 상권데이터에 맞춰서 코드가 수정된 버전임

JSON의 인코딩은 ansi로 저장할 것


#choropleth 함수 색은 아래 사이트에서 확인
http://colorbrewer2.org
색 종류중에 sequential 선택할 것

"""
import pandas as pd
import folium
import os

############################################
#서울시 지도 데이터 만드는 법
############################################

if not os.path.isfile("seoul_sample_data.xlsx"):
    datafile = r"D:\ZZ.lecture\2차수\Data\상가업소정보_2017년_9월\상가업소_201709_01.csv"
    df = pd.read_csv(datafile, engine="python")
    dfa = df[["상호명", "시군구코드"]][df.상호명.notnull() & df.상호명.str.contains("스타벅스")]
    gp = dfa.groupby(["시군구코드"]).count()
    dfb = gp.reset_index()
    dfb.columns = ["code", "amount"]
    dfb.code = dfb.code.astype(str)

    dfb.to_excel("seoul_sample_data.xlsx")
else:
    dfb = pd.read_excel("seoul_sample_data.xlsx")
    dfb.code = dfb.code.astype(str)

map = folium.Map(location=[37.33, 126.58], zoom_start=10)
geo_data = "seoul.json"
map.choropleth(geo_data=geo_data, data=dfb,
               columns=['code', 'amount'],
               key_on='feature.properties.SIG_CD',
               fill_color='BuPu', legend_name='스타벅스업장매장수')

map.save("서울 스타벅스 분포도.html")

############################################
#전국 지도 데이터 만드는 법
############################################

datafiles = [r"D:\ZZ.lecture\2차수\Data\상가업소정보_2017년_9월\상가업소_201709_01.csv",
r"D:\ZZ.lecture\2차수\Data\상가업소정보_2017년_9월\상가업소_201709_02.csv",
r"D:\ZZ.lecture\2차수\Data\상가업소정보_2017년_9월\상가업소_201709_03.csv",
r"D:\ZZ.lecture\2차수\Data\상가업소정보_2017년_9월\상가업소_201709_04.csv"]

if not os.path.isfile("korea_sample_data.xlsx"):
    df_list = []
    for datafile in datafiles:
        df = pd.read_csv(datafile, engine="python")
        dfa = df[["상호명", "시도코드"]][df.상호명.notnull() & df.상호명.str.contains("치킨")]
        df_list.append(dfa)

    dfa = pd.concat(df_list)
    gp = dfa.groupby(["시도코드"]).count()
    dfb = gp.reset_index()
    dfb.columns = ["code", "amount"]
    dfb.code = dfb.code.astype(str)

    dfb.to_excel("korea_sample_data.xlsx")
else:
    dfb = pd.read_excel("korea_sample_data.xlsx")
    dfb.code = dfb.code.astype(str)

map = folium.Map(location=[37.33, 126.58], zoom_start=10)
geo_data = "skorea_provinces_geo_simple.json"
map.choropleth(geo_data=geo_data, data=dfb,
               columns=['code', 'amount'],
               key_on='feature.properties.code',
               fill_color='GnBu', legend_name='치킨업장매장수')

map.save("전국치킨분포도.html")
#http://colorbrewer2.org
