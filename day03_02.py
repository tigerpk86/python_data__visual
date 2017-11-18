#!__*__coding:utf-8__*__
# pytagcloud 설치 방법
# 아나콘다
#pip install -U pytagcloud
#pip install -U pygame
#pip install -U simplejson

#pip install -U konlpy

from pytagcloud import create_tag_image, make_tags
import collections

a = ["한", "한", "1" , "1", "1", "1", "1", "2", "2", "2", "2", "2", "2", "2", "3", "3", "3", "3", "3"]
counter = collections.Counter(a);
h = counter.most_common();
print(counter)
b = make_tags(h, maxsize=50)
create_tag_image(b, "my_output.png",size=(1000, 500), background=(255,0,0),  fontname="hangle");