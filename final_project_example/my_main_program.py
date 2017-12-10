#!__*__coding:utf-8__*__
import os
import sys
import cmd
import sub_calculate_100days
import sub_pytagcloud as dd
import sub_naver_search_blog as naver_blog
import sub_naver_search_news as naver_news

class MyShell(cmd.Cmd):
    intro = """==========================
    데이터 분석 프로그램 v1.0
    ======================
    """
    prompt = "(명령어를 입력해 주십시오)>>"

    def do_home(self, arg):
        """첫 메뉴로 갑니다."""
        print("do home입니다.")

    def do_makereport(self, arg):
        """이 것은 레포트를 만드는 것입니다."""
        print("AAAA")

    def do_blog(self, arg):
        """
        네이버 블로그에서 해당 키워드를 검색합니다.
        """
        keyword = input("검색 키워드를 입력해 주십시오:")
        naver_blog.search_blog_main(keyword)

    def do_news(self, arg):
        """
        네이버 뉴스에서 해당 키워드를 검색합니다.
        """
        keyword = input("검색 키워드를 입력해 주십시오:")
        naver_news.search_news_main(keyword)

    def do_quit(self, arg):
        """
        프로그램을 종료합니다.
        """
        print("프로그램을 종료합니다.")
        return True

    def do_caldate(self, arg):
        """
        만나지 천일을 계산합니다.
        """
        sub_calculate_100days.cal_date()

    def do_sn(self, arg):
        """
        CSV 파일을 읽어서 2번째 컬럼의 항목으로 pytagcloud를 만듭니다. 
        """
        x = dd.get_top_100()
        if x != -99: #[(사랑, 100)
            dd.draw_graph(x)

if __name__ == "__main__":
    MyShell().cmdloop()