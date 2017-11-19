#!__*__coding:utf-8__*__

import pandas as pd
import os
import glob


top_dir = "C:\\Users\\505\\Downloads\\상가업소_201609\\"
file_names = glob.glob(os.path.join(top_dir, "*.csv"))
a = []
for filename in file_names :
    df = pd.read_csv(filename,  engine="python")
    #df = pd.read_csv(filename, nrows=10, engine="python")
    a.append(df)

df = pd.concat(a)

starbucks = df[df.상호명.notnull() & df.상호명.str.contains("스타벅스")]
#starbucks["강남"] = starbucks.시도명.apply(is_gangnam)
g2 = starbucks.groupby(["시도명", "시군구명"])
df2 = g2.count()
df2.to_excel("전국.xlsx")
print(df2)



