import pandas as pd

def conv_province(i) :
    if len(i) == 4 & i[-1] == "도" :
        return i[0] + i[2]
    else :
        return i.str.split(" ")[0]

criminal_path = "D:\\python\\범죄발생\\2015년_범죄발생지_지역별.csv"

df = pd.read_csv(criminal_path, engine="python")
dfa = df.T
dfb = dfa.iloc[3:-2]
dfb["지역명"] = dfb.index
dfb["그룹명"] = dfb.지역명.agg(lambda x: x.split(" ")[0])
dfb[8] = dfb[8].astype(int)
dfc = dfb.groupby(["그룹명"]).sum()

people_path = "D:\\python\\201612_201612_주민등록인구및세대현황_연간.csv"

#dfc.to_excel("1단계.xlsx")
#!1단계.xlsx