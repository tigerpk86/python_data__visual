#!__*__coding:utf-8__*__
import csv
import collections
from pytagcloud import create_tag_image, make_tags

a = "스타 스타 크리스마스 스타 크리스마스 스타"
b = a.split();
c = collections.Counter(b)
print(type(c))
print(c)
x = c.most_common(10)
print(type(x))
print(x)
d = make_tags(x, maxsize=100)
print(type(d))
print(d)
create_tag_image(d, "star.jpg", size=(1000,500), fontname='hangle')
