#!__*__coding:utf-8__*__

# employeeNames = ["andrew", "edward", "thomas"]
employeeNames = {"andrew": ["it","com0101","seoul"], "edward":"edward", "thomas":"thomas"}
# inputName = input("이름을 입력해주세요.")
inputName = "andrEw     "
inputName = inputName.strip().lower()
employeeInfo =  employeeNames[inputName];
print (employeeInfo);


