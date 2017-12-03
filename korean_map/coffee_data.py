import os
import pandas as pd
import matplotlib.pyplot as plt

file = u"C:\\Users\\505\\Downloads\\상가업소_201609\\상가업소_201609_%s.csv"
# file = "C:\\git\\python_data__visual\\korean_map\\result.xlsx"

pds = []
for i in range(1, 4):
    one_file = file % str(i).zfill(2)
    x = pd.read_csv(one_file, engine="python")
    pds.append(x)
df = pd.concat(pds)
dfa = df[df.시도명 == "서울특별시"]

starbucks = dfa[dfa.상호명.notnull() & dfa.상호명.str.contains("스타벅스")]
starbucks = starbucks[["시군구명"]]
starbucks["스타벅스"] = "스타벅스"
starbucks = starbucks.groupby(["시군구명"]).count()
starbucks = starbucks.reset_index()


hollis = dfa[dfa.상호명.notnull() & dfa.상호명.str.contains("할리스")]
hollis = hollis[["시군구명"]]
hollis["할리스"] = "할리스"
hollis = hollis.groupby(["시군구명"]).count()
hollis = hollis.reset_index()

dfa2 = starbucks.merge(hollis, on=["시군구명"])
dfa2.to_excel("result.xlsx")


