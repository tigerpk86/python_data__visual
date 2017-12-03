import pandas as pd
from konlpy.tag import Kkma
from konlpy.utils import pprint
df = pd.read_excel("박근혜_뉴스검색결과_with내용.xlsx")
kkma = Kkma()
for i in range(len(df)):
    a = kkma.nouns(df.iloc[i].comment)
    print(a)
