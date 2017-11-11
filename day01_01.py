#!__*__coding:utf-8__*__

sexInfo = {"1":"남자", "2":"여자", "3":"남자", "4":"여자"}

userInfo = input("input your jumin")
birthYear = userInfo[0:2];
birthMotnth = userInfo[2:4];
birthDay = userInfo[4:6];
userSexInfo = sexInfo[userInfo[7]];

userBirthDayInfoMessage = "귀하의 생년월일은 " + birthYear + "년 " + birthMotnth + "월 " + birthDay +"일 입니다.";
userSexInfoMessage = "귀하의 성별은 " + userSexInfo + "입니다."

print (userBirthDayInfoMessage);
print (userSexInfoMessage);
