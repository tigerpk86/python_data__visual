#!__*__coding:utf-8__*__

import os
import pandas as pd
import matplotlib.pyplot as plt

file = u"C:\\Users\\505\\Downloads\\상가업소_201609\\상가업소_201609_%s.csv"

pds = []
for i in range(1, 4):
    one_file = file % str(i).zfill(2)
    x = pd.read_csv(one_file, engine="python")
    pds.append(x)
z1 = pd.concat(pds)


for i in z1.columns:
    print(">>" + i + "<<")
    starbucks = z1[z1.표준산업분류명.notnull() & z1.표준산업분류명.str.contains("치킨 전문점")]  # ".str.contains("스타벅스")]
    starbucks.to_excel(".\\chicken_201706.xlsx")

    starbucks = starbucks[["표준산업분류명", "시도명", "시군구명"]]
    starbucks = starbucks.groupby(["시도명", "시군구명"]).count()
    starbucks = starbucks.reset_index()

    ######################################
    csv = r"data_draw_korea.csv"

    m = pd.read_csv(csv, encoding="utf-8", engine="python")
    print(m)

    yy = starbucks.merge(m, how='right', left_on=['시도명', '시군구명'], right_on=['광역시도', '행정구역'])
    print(yy)


    def convert_float(i):
        i = i.replace(",", "")
        if i.isdigit():
            return float(i)
        else:
            return 0


    yy.to_excel("chicken_지역별_상점수_2017.xlsx")

    import korea_showMap

    korea_showMap.drawKorea("표준산업분류명", yy, "광역시도", "행정구역", "Reds")


