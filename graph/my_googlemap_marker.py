#!__*__coding:utf-8__*__

"""
프로그램 설치
pip install folium

#기본 설명은 여기 있음
http://folium.readthedocs.io/en/latest/quickstart.html

#아이콘 종류는 아래 웹사이트에서 확인
http://fontawesome.io/
prefix = "fa" 사용할것


"""
import pandas as pd
import folium
import os

datafiles = [r"D:\ZZ.lecture\2차수\Data\상가업소정보_2017년_9월\상가업소_201709_01.csv",
r"D:\ZZ.lecture\2차수\Data\상가업소정보_2017년_9월\상가업소_201709_02.csv",
r"D:\ZZ.lecture\2차수\Data\상가업소정보_2017년_9월\상가업소_201709_03.csv",
r"D:\ZZ.lecture\2차수\Data\상가업소정보_2017년_9월\상가업소_201709_04.csv"]

if not os.path.isfile("korea_google_marker.xlsx"):
    df_list = []
    for datafile in datafiles:
        df = pd.read_csv(datafile, engine="python")
        dfa = df[["상호명", "위도", "경도"]][df.상호명.notnull() & (df.상호명.str.contains("네네치킨") | df.상호명.str.contains("교촌치킨"))]
        df_list.append(dfa)

    dfa = pd.concat(df_list)
    dfa.to_excel("korea_google_marker.xlsx")
else:
    dfa = pd.read_excel("korea_google_marker.xlsx")

#############################################################################################################
# 마커 찍기 샘플
#############################################################################################################

map_1 = folium.Map(location=[37.33, 126.58], zoom_start=8)

for i in range(len(dfa)):
    name = dfa.iloc[i].상호명
    m = dfa.iloc[i].위도
    n = dfa.iloc[i].경도

    if name.find("네네치킨") >= 0:
        folium.Marker([m, n], popup=name, icon=folium.Icon(icon='spoon', prefix='fa', color='green')).add_to(map_1)
    else:
        folium.Marker([m, n], popup=name, icon=folium.Icon(icon='wrench', prefix='fa', color='red')).add_to(map_1)

map_1.save("folium_네네치킨_교촌치킨.html")


#############################################################################################################
# 맵 타일 샘플
#############################################################################################################

map_2 = folium.Map(location=[37.33, 126.58], zoom_start=10, tiles='Stamen Terrain')

cnt = 0
for i in range(len(dfa)):
    cnt += 1
    if cnt > 10:
        break
    name = dfa.iloc[i].상호명
    m = dfa.iloc[i].위도
    n = dfa.iloc[i].경도

    if name.find("네네치킨") >= 0:
        folium.Marker([m, n], popup=name, icon=folium.Icon(icon='spoon', prefix='fa', color='green')).add_to(map_2)
    else:
        folium.Marker([m, n], popup=name, icon=folium.Icon(icon='wrench', prefix='fa', color='red')).add_to(map_2)

map_2.save("folium_네네치킨_교촌치킨_StamenTerrain_타일적용.html")

#############################################################################################################
# 맵 타일 샘플
#############################################################################################################

map_2 = folium.Map(location=[37.33, 126.58], zoom_start=10, tiles='Stamen Toner')

cnt = 0
for i in range(len(dfa)):
    cnt += 1
    if cnt > 10:
        break
    name = dfa.iloc[i].상호명
    m = dfa.iloc[i].위도
    n = dfa.iloc[i].경도

    if name.find("네네치킨") >= 0:
        folium.Marker([m, n], popup=name, icon=folium.Icon(icon='spoon', prefix='fa', color='green')).add_to(map_2)
    else:
        folium.Marker([m, n], popup=name, icon=folium.Icon(icon='wrench', prefix='fa', color='red')).add_to(map_2)

map_2.save("folium_네네치킨_교촌치킨_StamenToner_타일적용.html")