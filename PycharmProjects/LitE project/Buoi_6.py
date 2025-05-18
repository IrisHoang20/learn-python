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
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def greet(self):
#         print(f"Hello, my name is {self.name} and I'm {self.age} year old")
#
# class Student(Person):
#     def __init__(self, name, age, student_id):
#         super().__init__(name, age)
#         self.student_id = student_id
#     def display(self):
#         print(f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}")
#
# SV_01 = Student('Iris', '33', 'ST_001')
# SV_01.display()
# SV_01.greet()

"""tính trừu tượng"""
from threading import settrace_all_threads

# from abc import ABC, abstractmethod
#
# class PersonAbstract(ABC):
#     name = None
#     age = 0
#
#     def getName(self):
#         print(self.name)
#
#     def getAge(self):
#         print(self.age)
#
#     @abstractmethod
#     def getFull(self):
#         pass
#
#     @abstractmethod
#     def showInfor(self):
#         pass
#
# class Person(PersonAbstract):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def getFull(self):
#         self.getName()
#         self.getAge()
#
#     def showInfor(self):
#         print(self.name)
#         print(self.age)
#
#     def setInfor(self, name, age):
#         self.name = name
#         self.age = age
#
# a = Person('Hoàng Thị Hoa', '33')
# a.getFull()
# a.setInfor('Nha Trang - Khánh Hòa', 50)
# a.showInfor()

"""BÀI TẬP"""
from abc import ABC, abstractmethod

class VehicleAbstract(ABC):
    brand = None
    model = None
    year = 0

    def getBrand(self):
        print(self.brand)

    def getModel(self):
        print(self.model)

    def getYear(self):
        print(self.year)

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    @abstractmethod
    def get_info(self):
        pass

class Car(VehicleAbstract):
    def __init__(self, brand, model, year, seat):
        self.brand = brand
        self.model = model
        self.year =  year
        self.seat = seat

    def getSeat(self):
        print(self.seat)

    def start_engine(self):
        print('Khởi tạo')

    def stop_engine(self):
        print('Kết thúc')

    def get_info(self):
        self.getBrand()
        self.getModel()
        self.getYear()
        self.getSeat()

    def showInfo(self):
        print(self.brand)
        print(self.model)
        print(self.year)
        print(self.seat)

car_01 = Car('Toyota', 'TY_0012', '2025', '29')
car_01.start_engine()
car_01.showInfo()
car_01.stop_engine()


class Motorcycle(VehicleAbstract):
    def __init__(self, brand, model, year, type):
        self.brand = brand
        self.model = model
        self.year = year
        self.type = type


