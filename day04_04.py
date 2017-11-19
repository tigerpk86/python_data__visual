#!__*__coding:utf-8__*__
## 성적표로 석차, 평균, 총점 계산 및 그래프

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

def set_font_config() :
    font_location = "c:\\windows\\fonts\\malgun.ttf"
    font_name = font_manager.FontProperties(fname=font_location).get_name()
    matplotlib.rc('font', family=font_name)

def read_and_aggreate() :
    filename = "성적표.xlsx"
    dfa = pd.read_excel(filename)
    # columns = list(df.columns)
    subjects = ['국어', '영어', '수학', '과학']
    dfa["총점"] = dfa[subjects].sum(axis = 1)
    dfa["평균"] = dfa[subjects].mean(axis = 1)
    #정렬
    dfb = dfa.sort_values(["총점"], ascending=False)
    dfb["석차"] = list(range(1, len(dfb)+1))
    dfb.to_excel("text4.xlsx")

    dfb.index = dfb.이름
    dfc = dfb[['국어', '영어', '수학', '과학']]
    dfc.plot(kind="bar")
    #dfc.plot(kind="scatter", x="국어", y="영어)
    #dfc.plot(kind="line")
    #plt.show()
    plt.savefig("TEST4.PNG")


if __name__ == "__main__" :
    set_font_config()
    read_and_aggreate()
#









