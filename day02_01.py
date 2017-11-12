#!__*__coding:utf-8__*__
import csv
import os


    def searchEmployee() :
        global  emplyee_dic
        print("검색")
        keyword = input("사번 입력: ");
        if keyword in emplyee_dic:
            print (emplyee_dic[keyword][0] , emplyee_dic[keyword][1])

    def registerEmployee() :
        global emplyee_dic
        print("등록")
        id = input("사번 입력 : ")
        name = input("이름 입력 : ")
        div = input("부서 입력 : ")
        emplyee_dic[id] = [name, div];

    def deleteEmployee() :
        global  emplyee_dic
        print("퇴사")
        keyword = input("사번 입력: ");
        emplyee_dic.pop(keyword);


    def loadEmployeeAddress() :
        print ("주소록 불러오기")

    def saveEmployeeAddress() :
        print ("주소록 저장")

    def selectNumber() :
        print (""" 직원 주소록 만들기
            1. 직원 검색
            2. 직원등록
            3. 직원삭제
            4. 주소록 로드
            5. 주소록 저장
            6. 프로그램 종료 """)
        return input("입력:=> ");

    def loadEmployeeInfo() :
        global filename
        global emplyee_dic

        if os.path.isfile(filename) :
            f_in = open(filename);
            f_csv_in = csv.reader(f_in);
            for line in f_csv_in :
                emplyee_dic[line[0]] = [line[1], line[2]]
            f_in.close()

    def saveEmployeeInfo() :
        global filename
        global emplyee_dic

        f_out = open(filename, "w");
        for emplyee_no in emplyee_dic.keys() :
            result = "%s,%s,%s" % (emplyee_no,emplyee_dic[emplyee_no][0], emplyee_dic[emplyee_no][1])
            f_out.write(result);
        f_out.close()


if __name__ == "__main__":
    filename = "C:\\Users\\505\\Desktop\\test\\employee.csv"
    emplyee_dic = {}

    loadEmployeeInfo();

    while True:
        select_number = selectNumber();
        if select_number == "1":
            searchEmployee();
        elif select_number == "2":
            registerEmployee();
        elif select_number == "3":
            deleteEmployee();
        elif select_number == "4":
            loadEmployeeInfo();
        elif select_number == "5":
            saveEmployeeInfo();
        elif select_number == "6":
            print ("종료 입력하셨습니다.")
            break;
        else:
            print("잘못 입력");



