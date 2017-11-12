#!__*__coding:utf-8__*__
import csv
import time
import os
import collections

store_name_list = [];
store_name_count = {};
store_count_dic = [];

def search(dirname):
    filenames = os.listdir(dirname)
    full_filename = [];
    for filename in filenames:
        full_filename.append(os.path.join(dirname, filename))
    return full_filename

def readFile(full_filenames) :
    for filename in full_filenames:
        print("start: " + str(time.time()))
        store_info_file = open(filename)
        store_info_file_csv = csv.reader(store_info_file);

        for i in store_info_file_csv:
            store_name_list.append(i[1]);
            if i[1] in store_name_count:
                store_name_count[i[1]] = store_name_count[i[1]] + 1;
            else:
                store_name_count[i[1]] = 1;

        store_info_file.close();
        print("ended: " + str(time.time()))

def findStoreCount() :
    while True :
        keyword = input("입력 : ")
        print(store_name_count[keyword]);

def saveFile(filename):
    f = open( "C:\\Users\\505\\Desktop\\test\\"+ filename, "w");
    print(store_count_dic)
    for (name, count) in store_count_dic :
        f.write("%s: %d\n" % (name, count));
    f.close();


full_filenames = search("C:\\Users\\505\\Desktop\\상가업소정보__2016년_9월_\\");
readFile(full_filenames);
store_count_dic = collections.Counter(store_name_count);
store_count_dic = store_count_dic.most_common(50)
saveFile("test.txt")

# findStoreCount();


