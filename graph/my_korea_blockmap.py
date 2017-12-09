#!__*__coding:utf-8__*__

"""
프로그램 설치

Korea_showMap.drawKorea 함수를 쓰면 된다.
data_draw_korea.csv 파일을 항상 같이 가지고 다녀야 한다.
data_draw_korea.csv에 있는 면적 부분의 데이터만 변경되면 사용할 수 있다.

지도 색은 여기서 고를 수 있다.
https://matplotlib.org/examples/color/colormaps_reference.html
https://matplotlib.org/_images/colormaps_reference_01.png 이것 참조할 것

문제- 수원이 정말 치킨집이 하나도 없을까? 데이터를 분석해서 해결한다.

"""
import os
import pandas as pd
import korea_showMap

#######################################################################
# 기본 csv 파일로 지도 만드는 샘플
#######################################################################
csv = r"data_draw_korea.csv"

m = pd.read_csv(csv, encoding="utf-8", engine="python")
print(m)

korea_showMap.drawKorea('면적', m, '광역시도', '행정구역', 'OrRd')


#######################################################################
# 기본 csv 파일로 지도 만드는 샘플
#######################################################################

datafiles = [r"C:\Users\505\Downloads\상가업소_201609\상가업소_201609_01.csv",
r"C:\Users\505\Downloads\상가업소_201609\상가업소_201609_02.csv",
r"C:\Users\505\Downloads\상가업소_201609\상가업소_201609_03.csv",
r"C:\Users\505\Downloads\상가업소_201609\상가업소_201609_04.csv"]

# if not os.path.isfile("korea_blockmap.xlsx"):
df_list = []

def a(i):
    if i == "세종특별자치시" :
        return "세종시"
    return i.split()[0];

for datafile in datafiles:
    df = pd.read_csv(datafile, engine="python")
    # df.시군구명 = df.시군구명.agg(lambda x: x.split(" ")[0])
    df.시군구명 = df.시군구명.agg(a)
    dfa = df[["상호명", "시도명", "시군구명"]][df.상호명.notnull() & df.상호명.str.contains("치킨")]
    df_list.append(dfa)

dfa = pd.concat(df_list)
dfb = dfa.groupby(["시도명", "시군구명"]).count()
dfb = dfb.reset_index()
dfb.to_excel("korea_blockmap.xlsx")
# else:
#     dfb = pd.read_excel("korea_blockmap.xlsx")
#     dfb = dfb.reset_index()
#     print(dfb.columns)

csv = r"data_draw_korea.csv"
m = pd.read_csv(csv, encoding="utf-8", engine="python")
print(m)

yy = dfb.merge(m,  how='outer', left_on=['시도명', '시군구명'], right_on=['광역시도', '행정구역'])
yy.to_excel("korea_blockmap_merged.xlsx")

korea_showMap.drawKorea('상호명', yy, '광역시도', '행정구역', 'OrRd')

