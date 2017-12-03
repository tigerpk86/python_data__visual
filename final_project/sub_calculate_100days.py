#!__*__coding:utf-8__*__
import datetime
from dateutil.parser import parse

def cal_date():
    a = input("처음 언제 만나셨어요(yyyy-mm-dd):")
    first_date = parse(a)
    t_day = datetime.timedelta(days=1000)
    new_date = first_date + t_day

    weeks = ["월", "화", "수", "목", "금", "토", "일"]

    result_string = "%s년 %s월 %s일에 천일 이시군요" % (new_date.year, new_date.month, new_date.day)
    result2_string = "%s요일이시군요" % weeks[new_date.weekday()]
    print(result_string)
    print(result2_string)

    h1 = datetime.datetime.now() - first_date
    print("%s일 되셨군요" % h1.days)