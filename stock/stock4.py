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
from pandas import Series, DataFrame


def getMAx(df):
    count = 0;
    maxVal = 999999999;
    prevVal = maxVal
    startDate = ""

    for i in range(len(df)):
        a = df.iloc[i]
        curVal = a.Close;
        if curVal < prevVal:
            if count == 0:
                startDate = a.Date
            count = count + 1;
        else:
            if count >= 10:
                print(startDate + " ~ " + a.Date + " - " + str(count))
            count = 0;
        prevVal = curVal;


jongmok_filename = "종목표.xlsx"
url = "http://bigdata-trader.com/itemcodehelp.jsp"

KOSPI_df = pd.read_excel("C:\\git\\python_data__visual\\stock\\stok_file\\KOSPI.xlsx")

if not os.path.isfile(jongmok_filename):
    df = pd.read_html(url)
    df = df[0]
    df.to_excel(jongmok_filename)
else:
    df = pd.read_excel(jongmok_filename)

df.columns = ["종목코드", "종목명", "종류"]

dic_stock = {'종목코드': [], '종목명': [], '상관계수': []};
for i in range(len(df)):
    a = df.iloc[i];
    if a.종류 == "KOSPI":
        file_name = "C:\\git\\python_data__visual\\stock\\stok_file\\" + a.종목코드 + ".xlsx";
        if not os.path.isfile(file_name):
            continue

        df_157 = pd.read_excel(file_name);
        getMAx(df_157)

