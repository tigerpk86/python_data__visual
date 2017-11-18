#!__*__coding:utf-8__*__
import os
import sys
import cmd
import market_info
from pytagcloud import create_tag_image, make_tags
import collections
# sys.path
# import sys.append("aaasdfa")


class MyShell(cmd.Cmd) :
    intro = """제 프로그램 입니다."""
    prompt = "명령어 입력 >> "

    def do_home(self, arg):
        """ 홈으로 """
        print("do home")

    def do_quit(self):
        """ 종료 """
        return True

    def do_read_market_info(self, arg):
        """상권정보 가져오기"""
        #상가업소_201609_01.csv
        colum_infos = market_info.get_colum_infos_from_file("C:\\Users\\505\\Downloads\\상가업소_201609\\" + str(arg), 1);
        colum_info_counter_list = market_info.get_most_info_from_list(colum_infos, 100);
        market_info.make_tag_cloud_image(colum_info_counter_list)

if __name__ == "__main__":
    MyShell().cmdloop()

# 구글 코스피 정보
# http://finance.gogle.com/finance/historical?q=KRX%3AKOSPI&output=csv

