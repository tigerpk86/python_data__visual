#!__*__coding:utf-8__*__
import glob
import pandas as pd
import os
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager


import matplotlib.font_manager as font_manager

def set_font_config() :
    font_location = "c:\\windows\\fonts\\malgun.ttf"
    font_name = font_manager.FontProperties(fname=font_location).get_name()
    matplotlib.rc('font', family=font_name)


############
# 각년도의 서울시의 구에 존재하는 스타벅스 갯수를 엑셀에 저장
############
dirs = ["C:\\Users\\505\\Desktop\\양진이\\상가업소_201512\\",
        "C:\\Users\\505\\Desktop\\양진이\\상가업소_201609\\",
        "C:\\Users\\505\\Desktop\\양진이\\상가업소_201706\\"
       ];


def refineDataAndSaveCsv(dir, year) :
    file_list = glob.glob(dir + "*.csv");
    dfs = [];

    for file_name in file_list :
        print(file_name);
        df = pd.read_csv(file_name, engine="python");
        df = df[["시도명", "시군구명", "상호명"]][df.상호명.notnull() & df.상호명.str.contains("스타벅스") & df.시도명.str.contains("서울")]
        df["상호명"] = "스타벅스"
        dfs.append(df);
    all_df = pd.concat(dfs);
    count_df = all_df .groupby(["시도명", "시군구명"]).count()
    count_df.to_csv("refineData_" + str(year)+".csv")



#######################
## 각 년도의 countt수를 머지해서 csv포맷으로 저장
#######################
refined_data_dirs = "C:\\git\\python_data__visual\\final_projet\\"
def mergeResultDataOnlySeoul(dir) :
    file_list = glob.glob(dir + "refineData*.csv");


    is_start = True;
    for file_name in file_list :
        name = os.path.basename(file_name)
        name = name.split("_")[1].split(".")[0]
        if is_start  == True:
            result_df = pd.read_csv(file_name , engine="python");
            result_df.columns = ['시도명', '시군구명', name]
            is_start = False;
        else :
            df = pd.read_csv(file_name, engine="python")
            df.columns = ['시도명', '시군구명', name]
            result_df = result_df.merge(df, how="outer", on=['시도명', '시군구명'])
    result_df.to_csv("final_result.csv")

refined_data_dirs = "C:\\git\\python_data__visual\\final_projet\\final_result.csv"
def showGraph(file_name) :
    df = pd.read_csv(refined_data_dirs, engine="python")
    df = df[["시도명", "시군구명", "2015", "2016", "2017"]]
    df.index = df.시군구명
    df.plot(kind="bar", title='스타벅스')
    plt.show()


def showIncreasingGrpah(filename):
    df = pd.read_csv(filename, engine="python");
    inc_rate_dic = {
        "시군구명": [],
        "rate": []
    }
    for i in range(len(df)):
        cur = df.iloc[i];

        inc_rate_dic["시군구명"].append(cur.시군구명);
        inc_rate_dic["rate"].append((cur["2017"] / cur["2016"])*100);
    result_df = pd.DataFrame(inc_rate_dic)
    result_df.index = result_df.시군구명;
    result_df.plot(kind="barh", title='스타벅스');
    plt.show()
    #result_df.to_csv("result_incresing.csv")




set_font_config();


## merge
# year = 2015;
# for dir in dirs :
#     refineDataAndSaveCsv(dir, year);
#     year = year + 1;

## count
# mergeResultDataOnlySeoul(refined_data_dirs)

## show bar graph
#showGraph(refined_data_dirs)

## show bar increase graph
#showIncreasingGrpah(refined_data_dirs);