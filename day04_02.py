import pandas as pd
import pandas_datareader

def fx(i):
    a = ["삼성", "현대", "LG", "롯데", "한국전력", "GS"]
    for j in a:
        if i.find(j) != -1:
            return j
    return "미분류"

def axss(i):
    return i

#itemcode_url = "http://bigdata-trader.com/itemcodehelp.jsp"
pd.read_csv("주가종목.xlxs")
d = pd.read_html(itemcode_url)[0];
d.columns = ["종목코드", "종목명", "종류"]
samsung = d[(d.종류 == "KOSPI") & (d.종목명.str.contains("삼성"))]
samsung.index = range(1, len(samsung)+1);
samsung["정보"] = "%s:%s" % (samsung.종류.apply(axss), samsung.종목코드.apply(axss))

for i in range(1, len(samsung)+1):
  #  result = "%s:%s" %(samsung.ix[i].종류, samsung.ix[i].종목코드)
 #   finename = "%s_%s" %(samsung.ix[i].종류, samsung.ix[i].종목코드)
#    df = pandas_datareader.get_data_google(result)
#    df.to_excel(finename + ".xlsx")
#    print(finename)
    pass

