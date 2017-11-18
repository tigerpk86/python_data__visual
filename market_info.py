import csv
import collections
from pytagcloud import create_tag_image, make_tags
import collections


def get_colum_infos_from_file(filename, column_index):
    coumln_info_list= []
    try :
        fopen = open(filename, "r")
    except :
        print("filename error")
    else :
        fopen_csv = csv.reader(fopen)
        for line in fopen_csv:
            coumln_info_list.append(line[column_index])
        fopen.close()
        return coumln_info_list

def get_most_info_from_list(coumln_info_list, count):
    return collections.Counter(coumln_info_list).most_common(count)

def make_tag_cloud_image(info_list):
    imgage_filename = input("input file name >>")
    tag_info_list = make_tags(info_list, maxsize=50)
    create_tag_image(tag_info_list, imgage_filename + ".png", size=(1000, 500), background=(0, 0, 0), fontname="hangle");
    print("image success, filename : " + str(imgage_filename))

if __name__ == "__main__":
    colum_infos = get_colum_infos_from_file("C:\\Users\\505\\Downloads\\상가업소_201609\\상가업소_201609_01.csv", 1);
    colum_info_counter_list = get_most_info_from_list(colum_infos, 100);
    make_tag_cloud_image(colum_info_counter_list)
