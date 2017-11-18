#!__*__coding:utf-8__*__

class cal:
    def __init__(self, num1, num2):
        self.num1 = num1;
        self.num2 = num2;
        pass
    def add(self):
        return self.num1 + self.num2
    def minus(self):
        return self.num1 - self.num2
    def mul(self):
        return self.num1 * self.num2
    def device(self):
        return self.num1 / self.num2

class Emp:
    rate = 1.1
    def __init__(self, name):
        self.name = name

    def set_salary(self, salary):
        self.salary = salary

    def set_newprice(self):
        self.salary = self.rate + self.salary

if __name__ == "__main__" :
    print(Emp.rate)
    park = Emp("park")
    park.set_salary(600)
    print(park.salary)

    kim = Emp("kim")
    kim.set_salary(500)
    print(kim.salary)
