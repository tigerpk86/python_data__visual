#!__*__coding:utf-8__*__
import decimal

for i in range(1,10) :
    for j in range(1,10) :
        #print(i, "x", j, "=", i*j, end = ". ");
        print("%2d x%2d =%2d" % (j, i, i * j), end=", ");
        #print(i * j, end=" ");
    print("");
