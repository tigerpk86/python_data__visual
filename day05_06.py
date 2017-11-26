import pandas as pd
filename1 = "2015년 범죄발생지(지역별).csv"
df = pd.read_csv(filename1, engine="python")
dfa = df.T

def get_group(i):
    #서울 --> 서울
    #경기 고양 --> 경기
    j = i.split(" ")
    return j[0]

def con_v2(i):
    if len(i) == 4 and i[-1] == "도":
        return i[0] + i[2]
    else:
        return i[0:2]

def remove_comma(i):
    return i.replace(",", "")

dfa["지역명"] = dfa.index
dfa["그룹"] = dfa.지역명.agg(get_group)

dfa.to_excel("output.xlsx")
dfb = dfa.iloc[3:-2] #필요없는 줄 삭제
dfb[8] = dfb[8].astype(int) ## 문자열을 숫자로 변경해 줘용
gb = dfb.groupby("그룹").sum()
gb = gb.reset_index()
gb.columns = ["행정구역3", "절도건수"]

filename2 = "201710_201710_주민등록인구및세대현황_월간 (2).csv"
cf = pd.read_csv(filename2, engine="python")
cf["행정구역2"] = cf["행정구역"].agg(get_group)
cf["행정구역3"] = cf["행정구역2"].agg(con_v2)
final_df = cf.merge(gb, on="행정구역3", how="outer")
final_df["2017년10월_총인구수"] = final_df["2017년10월_총인구수"].agg(remove_comma)
final_df["2017년10월_총인구수"] = final_df["2017년10월_총인구수"].astype(int)
final_df["1000명당절도건수"] = final_df["절도건수"] / final_df["2017년10월_총인구수"] * 1000
final_df.to_excel("저장끝.xlsx")