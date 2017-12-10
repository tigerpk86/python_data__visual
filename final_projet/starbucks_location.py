#!__*__coding:utf-8__*__

import pandas as pd
import glob
import folium

dir = "C:\\Users\\505\\Desktop\\양진이\\상가업소_201706\\";
def refineDataAndSaveCsv(dir) :
    file_list = glob.glob(dir + "*.csv");
    dfs = [];
    for file_name in file_list :
        print(file_name);
        df = pd.read_csv(file_name, engine="python");
        df = df[["상호명", "경도", "위도"]][df.상호명.notnull() & df.상호명.str.contains("스타벅스")]
        dfs.append(df)
    result_dfs = pd.concat(dfs)
    result_dfs.to_csv("result_location.csv")


file_name = "C:\\git\\python_data__visual\\final_projet\\result_location.csv"
def showMarker(file_name) :
    dfa = pd.read_csv(file_name, engine="python")
    map_1 = folium.Map(location=[37.33, 126.58], zoom_start=8)
    for i in range(len(dfa)):
        cur = dfa.iloc[i]
        name = cur.상호명
        latitude = cur.위도
        longtude = cur.경도
        marker = folium.Marker([latitude, longtude], popup=name,
                               icon=folium.Icon(icon='spoon', prefix='fa', color='green'))
        marker.add_to(map_1)
    map_1.save("스타벅스.html")

refineDataAndSaveCsv(dir)
showMarker(file_name)
