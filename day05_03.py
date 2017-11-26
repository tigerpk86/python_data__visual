import folium as fl
import pandas as pd


# github에서 southkorea-maps
# color colrbrews

datafile="C:\\Users\\505\\Downloads\\상가업소_201609\\상가업소_201609_01.csv"
df = pd.read_csv(datafile, engine="python")

dfa = df[['상호명','시군구코드']][df.상호명.notnull()& df.상호명.str.contains("스타벅스")]

gp = dfa.groupby(["시군구코드"]).count()

dfb = gp.reset_index("시군구코드")
dfb.columns = ["code", "amount"]
dfb.code = dfb.code.astype(str)

map = fl.Map(location=[37.33, 126.58])

geo_data = "map_seoul.json"

map.choropleth(geo_data=geo_data,
               data=dfb, columns=["code", "amount"],
               key_on="feature.properties.SIG_CD",
               fill_color="BuPu",
               legend_name="sbuck")


map.save("sbuck.html")
# !sbuck.html


