import glob
import pandas as pd

files = glob.glob("C:\\git\\python_data__visual\\stock\\stok_file\\*xlsx")

def findRiseStock(files) :
    for file_name in files:
        try :
            df = pd.read_excel(file_name)
            is_okay = True
            for i in range(10):
                m = df.iloc[i].Close
                n = df.iloc[i+1].Close
                x = m - n
                if x < 0 :
                    is_okay = False
            if is_okay:
                print(file_name)
        except:
            print("에러파일 패스 : " + file_name)

def findSum(files) :
    for file_name in files:
        try :
            df = pd.read_excel(file_name)
            is_okay = True
            df = df.head(10)
            for i in range(len(df) - 1):
                m = df.iloc[i].Close
                n = df.iloc[i+1].Close
                x = m - n
                if x < 0 :
                    is_okay = False
            if is_okay:
                print(file_name)
        except:
            print("에러파일 패스 : " + file_name)



findRiseStock(files)