#!__*__coding:utf-8__*__
import csv
import collections
from pytagcloud import create_tag_image, make_tags

def get_top_100():
    filename = input("파일이름을 입력해 주십시오")
    try:
        f = open(filename, "r")
        a = []
        x = csv.reader(f)
        for i in x:
            a.append(i[1])
        f.close()
        b = collections.Counter(a)
        top_100 = b.most_common(100)
        return top_100 #[(사랑,100), (CU, 40)]
    except:
        print("파일 작업 중 에러가 발생했습니다.")
        return -99


def draw_graph(x):
    filename = input("최종 저장할 파일 이름을 입력해 주십시오")
    d = make_tags(x, maxsize=100)
    create_tag_image(d, filename, size=(1000,500), fontname='Malgun')
