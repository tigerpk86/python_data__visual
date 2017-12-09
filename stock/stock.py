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

jongmok_filename = "종목표.xlsx"
url = "http://bigdata-trader.com/itemcodehelp.jsp"

if not os.path.isfile(jongmok_filename):
    df = pd.read_html(url)
    df = df[0]
    df.to_excel(jongmok_filename)
else:
    df = pd.read_excel(jongmok_filename)

df.columns = ["종목코드", "종목명", "종류"]


########################################################
# KOSPI 주식 가져오기
########################################################

WebURL = "https://finance.google.com/finance/historical?q=%s&output=csv"

KOSPI = "KRX:KOSPI"
KOSPI_quote = urllib.parse.quote(KOSPI)
KOSPI_df = pd.read_csv(WebURL % KOSPI_quote)

pds = []
result = []
for i in range(len(df)):
    a = df.iloc[i];
    if a.종류 == "KOSPI":
        CODE_quote = urllib.parse.quote("KRX:" + str(a.종목코드));
        CODE_df = pd.read_csv(WebURL % CODE_quote);
        pds.append(CODE_df);
        time.sleep(1);
        result[a.종목코드] = df;

z1 = pd.concat(result)
z1.to_excel(".\\all_stock.xlsx")


############################
################
for i in range(len(df)):
    a = df.iloc[i];
    if a.종류 == "KOSPI":
        file_name = "C:\\git\\python_data__visual\\stock\stok_file\\" + a.종목코드 + ".xlsx";
        print(file_name)
        df_157 = pd.read_excel(file_name);
        yy = KOSPI_df.merge(df_157, on="Date");
        a = np.corrcoef(yy.Close_x, yy.Close_y);
        result = a[0][1];
        print(a.종목명 + " " + a.종목코드 + "" + str(result))
        import time
        time.sleep(5)
