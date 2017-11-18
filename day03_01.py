#!__*__coding:utf-8__*__

#pip install -U pytagcloude

import datetime
from dateutil.parser import parse

now = datetime.datetime.now();
print(now);


b = datetime.datetime(year=2010, month=12, day=30);


dt = parse("2016-12-06 14:30");
days_1000 = datetime.timedelta(days=1000);
print(dt - days_1000);

#input_data = input("언제 천일 됨? yyyy-mm-dd")
input_data = "2016-12-06";
first_dated_at = parse(input_data);
thounsand_day = datetime.timedelta(days=1000);
thounsand_date = first_dated_at  + thounsand_day;
message =  "%d년 %d월 %d일에 천일"
print(message % (thounsand_date.year, thounsand_date.month, thounsand_date.month));



