##############PYTHON CLASS & OBJECTS##################
###################class cho Student
# class Student:
#     school_name = 'Đại học quốc gia Hà Nội'
#
#     def __init__(self, name, age, birth_year, province):
#         self.name = name
#         self.age = age
#         self.birth_year = birth_year
#         self.province = province
#
#     def show_infor(self):
#         print(self.name)
#         print(self.age)
#         print(self.birth_year)
#         print(self.province)
#
# sinhvienA = Student("Tran Hanh", 42, 1984, "Hưng Yen")
# sinhvienA.show_infor()

########################class cho Car
# class Car:
#     def __init__(self, color, shape, brand):
#         self.color = color
#         self.shape = shape
#         self.brand = brand
#
#     def show_infor(self):
#         print(self.color)
#         print(self.shape)
#         print(self.brand)
#
# car_01 = Car('blue', 'round', 'Toyota')
# car_01.show_infor()

########################class cho bank account
# class BankAccount:
#     def __init__(self, balance, name):
#         self.__balance = balance
#         self.name = name
#
#     def get_balance(self):
#         return self.__balance
#
#     def deposit(self, balance):
#         self.__balance += balance
#
#     def set_balance(self, balance):
#         self.__balance = balance
#
# Iris_account = BankAccount(1000000, 'Iris')
# print(Iris_account.get_balance())


#############################class cho Sinh Viên
# class Students:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.__sex = sex
#     def get_sex(self):
#         return self.__sex
#
# Sv_01 = Students('Iris', '33', 'Female')
# print(Sv_01.name)
# print(Sv_01.age)
# print(Sv_01.get_sex())
#
# Sv_02 = Students('Jason', '25', 'Male')
# print(Sv_02.name)
# print(Sv_02.age)
# print(Sv_02.get_sex())

######################class cho xe
# class Motor:
#     def __init__(self, brand, color):
#         self.__brand = brand
#         self.color = color
#
#     def get_brand(self):
#         return self.__brand
#
#     def show_infor(self):
#         print(self.__brand)
#         print(self.color)
# xe_01 = Motor('Vinfast', 'Xanh')
# xe_01.show_infor()
# print(xe_01.color)
# print(xe_01.get_brand())

####################KẾ THỪA TRONG CLASS
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} year old")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    def display(self):
        print(f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}")

SV_01 = Student('Iris', '33', 'ST_001')
SV_01.display()
SV_01.greet()



