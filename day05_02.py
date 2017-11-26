import folium as fl
import pandas as pd
import numpy as np

def findCode(x) :
    if x.find("롯데리아") :
       return "롯데리아"
    elif x.find("맥도날드") :
        return "맥도날드"
    return "No"

datafile="C:\\Users\\505\\Downloads\\상가업소_201609\\상가업소_201609_01.csv"
df = pd.read_csv(datafile, engine="python")
hamberg = df[df.상호명.notnull() & (df.상호명.str.contains("맥도날드") | df.상호명.str.contains("롯데리아"))]

ham_loc = hamberg[["상호명","위도", "경도"]]

my_map = fl.Map(location=[37.5666, 126.97])
for i in range(len(ham_loc)):
    x = fl.Marker([ham_loc.iloc[i].위도, ham_loc.iloc[i].경도], popup=ham_loc.iloc[i].상호명)
    x.add_to(my_map)
my_map.save("map_output_02.html")

my_map.save("map_output_01.html")