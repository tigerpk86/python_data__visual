#!__*__coding:utf-8__*__
import pandas as pd
import pandas_datareader
import matplotlib as mat
import matplotlib.pyplot as plt
import numpy as np
import datetime
import urllib.parse
import os
import pickle
import time

########################################################
# 출력결과폴더
########################################################
excel_foler = "output\\excel"
result_folder = "output\\result"
if not os.path.isdir(excel_foler):
    os.makedirs(excel_foler)
if not os.path.isdir(result_folder):
    os.makedirs(result_folder)

########################################################
# 종목 코드 준비
# 실제 종목표.xlsx 파일이 있으면 웹에서 가져오지 않는다.
########################################################
jongmok_filename = "종목표.xlsx"
url = "http://bigdata-trader.com/itemcodehelp.jsp"

if not os.path.isfile(jongmok_filename):
    jongmok_filename_df = pd.read_html(url)
    jongmok_filename_df = jongmok_filename_df[0]
    jongmok_filename_df.to_excel(jongmok_filename)
else:
    jongmok_filename_df = pd.read_excel(jongmok_filename)

jongmok_filename_df.columns = ["종목코드", "종목명", "종류"]

########################################################
# KOSPI 주식 가져오기
########################################################

kospi_file = excel_foler + "\\kospi.xlsx"

if not os.path.isfile(kospi_file):
    WebURL = "https://finance.google.com/finance/historical?q=%s&output=csv"

    KOSPI = "KRX:KOSPI"
    KOSPI_quote = urllib.parse.quote(KOSPI)
    KOSPI_df = pd.read_csv(WebURL % KOSPI_quote)
    KOSPI_df.to_excel(kospi_file)
else:
    KOSPI_df = pd.read_excel(kospi_file)

########################################################
# 종목표에 있는 주식 코드를 하나씩 확인
########################################################

final_result = {}
jongmok_dic = {}

cnt = 0
for i in range(len(jongmok_filename_df)):
    a = jongmok_filename_df.iloc[i]
    h1 = a.종목코드
    h2 = a.종목명
    h3 = a.종류

    if h3 == "KOSPI":
        jongmok_dic[h1] = h2

        code_name = "KRX:" + h1
        code_name = urllib.parse.quote(code_name)

        jongmok_excel_file = excel_foler + "\\" + h1 + ".xlsx"
        print(jongmok_excel_file)
        if not os.path.isfile(jongmok_excel_file):
            try:
                df02 = pd.read_csv(WebURL % code_name)
            except:
                print("접속 에러 발생, 제외함")
                continue
            df02.to_excel(jongmok_excel_file)
        else:
            df02 = pd.read_excel(jongmok_excel_file)

        print(" ".join([h1, h2]))
        merged = KOSPI_df.merge(df02, on="Date")
        result = np.corrcoef(merged["Close_x"], merged["Close_y"])

        final_result[h1] = [merged, result]
        print(result)
        cnt += 1


########################################################
# 차트 한글 설정
########################################################
font_location = r"c:\windows\fonts\malgun.ttf"
font_name = mat.font_manager.FontProperties(fname=font_location).get_name()
mat.rc('font', family=font_name)



#####################################
# 상관계수를 넣기 위한 딕션너리생성
#####################################
data = {"code":[], "corrcoef":[]}

for i in final_result:
    data["code"].append(i)
    data["corrcoef"].append(final_result[i][1][0][1])

df = pd.DataFrame(data)
dfa = df.sort_values("corrcoef", ascending=False)


#####################################
# 그래프 및 차트 만들기
#####################################
top_10_dfa = dfa.head(10)
top_10_dfa.to_excel(result_folder + "\\상위_10개_종목.xlsx")

for i in range(10):
    codename = dfa.iloc[i].code
    df_01 = final_result[codename][0]
    ax = df_01.plot(kind="scatter", x="Close_x", y="Close_y", title= jongmok_dic[codename])
    ax.set_xlabel("코스피")
    ax.set_ylabel("종목종가")
    plt.savefig(result_folder + "\\상위종목_" + codename + ".png")


#####################################
# 하위 10개 상관계수가 놓은 종목
#####################################
bottom_10_dfa = dfa.head(10)
bottom_10_dfa.to_excel(result_folder + "\\하위_10개_종목.xlsx")

for i in range(10):
    j = len(dfa) - i - 1
    codename = dfa.iloc[j].code
    df_01 = final_result[codename][0]
    ax = df_01.plot(kind="scatter", x="Close_x", y="Close_y", title= jongmok_dic[codename])
    ax.set_xlabel("코스피")
    ax.set_ylabel("종목종가")
    plt.savefig(result_folder + "\\하위종목_" + codename + ".png")


#####################################
# 종가가 계속 상승한 종목
#####################################
#### 파일 리스트에서 파일을 하나씩 꺼내면서
import glob
files = glob.glob("output\\excel\\*.xlsx")

for one_file in files:
    df = pd.read_excel(one_file) #파일 하나 읽었음

    is_okay = True #파일 하나에 대한 isOkay = True
    df = df.head(10)
    for i in range(len(df)):
        if i == len(df)-1: #맨 마지막 줄인 경우에는 안 한다.
            pass
        else:
            m = df.iloc[i].Close
            n = df.iloc[i+1].Close
            x = m - n
            if x < 0:
                is_okay = False

    if is_okay:
        print("이 항목은 최근 마지막 10동안 금액이 계속 올랐습니다.")
        print(one_file)


#####################################
# 평균 거래량이 가장 많은 10개 종목
#####################################

jongmok_code = []
vol = []
a = []
b = []

for one_file in files:
    df = pd.read_excel(one_file) #파일 하나 읽었음
    is_okay = True #파일 하나에 대한 isOkay = True
    df = df.head(10)
    temp_i = []
    for i in range(len(df)):
        if i == len(df)-1: #맨 마지막 줄인 경우에는 안 한다.
            pass
        else:
            m = df.iloc[i].Volume
            temp_i.append(m)
    np.mean(m)
    jongmok_code.append(one_file)
    vol.append(m)
    a_temp = os.path.splitext(os.path.split(one_file)[1])[0]
    a.append(a_temp)
    try:
        b_temp = list(jongmok_filename_df[jongmok_filename_df.종목코드 == a_temp].종목명)[0]
    except:
        b_temp = ""
    b.append(b_temp)


data = {"파일명": jongmok_code,
        "거래량": vol,
        "종목코드": a,
        "종목명": b,
        }

dfc = pd.DataFrame(data, columns=["파일명", "종목코드", "종목명", "거래량"])
dfc = dfc.sort_values("거래량", ascending=False)
dfc.index = range(1, len(dfc) + 1)
dfc.to_excel(result_folder + "\\평균거래량높은 종목순 정렬.xlsx")