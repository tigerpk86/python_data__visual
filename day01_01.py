#!__*__coding:utf-8__*__
from datetime import datetime;

sexInfo = {"1":"남자", "2":"여자", "3":"남자", "4":"여자"}

#userInfo = input("input your jumin")
userInfo = "19860711-154"



birthYear = userInfo[0:2];
birthMotnth = userInfo[2:4];
birthDay = userInfo[4:6];
userSexInfo = sexInfo[userInfo[7]];


currentUserAge = (str)(2017 - int(birthYear));
#userBirthDayInfoMessage = "귀하의 생년월일은 " + birthYear + "년 " + birthMotnth + "월 " + birthDay +"일 입니다.";
userBirthDayInfoMessage = "귀하의 생년월일은 %-10s년 %s월 %s일 입니다." % (birthYear, birthMotnth, birthDay);

userSexInfoMessage = "귀하의 성별은 " + userSexInfo + "입니다."
userAgetInfoMessage = "귀하의 나이는 " + currentUserAge + "입니다."

print (userBirthDayInfoMessage);
print (userSexInfoMessage);
print (userAgetInfoMessage);
print (datetime.today().year);


