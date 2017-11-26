#!__*__coding:utf-8__*__

import pandas as pd
import os
import glob
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

def set_font_config() :
    font_location = "c:\\windows\\fonts\\malgun.ttf"
    font_name = font_manager.FontProperties(fname=font_location).get_name()
    matplotlib.rc('font', family=font_name)


def findCode(x) :
    if x.find("롯데리아") :
       return "롯데리아"
    elif x.find("맥도날드") :
        return "맥도날드"
    return "No"

set_font_config()
top_dir = "C:\\Users\\505\\Downloads\\상가업소_201609\\"
file_names = glob.glob(os.path.join(top_dir, "*.csv"))
a = []
for filename in file_names :
    df = pd.read_csv(filename,  engine="python")
#    df = pd.read_csv(filename, nrows=1000, engine="python")
    a.append(df)
df = pd.concat(a)

hamberg = df[df.상호명.notnull() & (df.상호명.str.contains("맥도날드") | df.상호명.str.contains("롯데리아"))]
hamberg = hamberg[["시도명", "시군구명", "상호명"]];
hamberg["계열"] = hamberg.상호명.agg(findCode)
df2 = hamberg.groupby(["시도명", "시군구명", "계열"]).count()
df2.to_excel("햄버거.xlsx")
df2.plot(kind="bar")
plt.show()




