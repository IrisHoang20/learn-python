class Student:
    school_name = ("Quoc Gia ha noi")

    def __init__(self, name, tuoi, nam_sinh, que_quan):
        self.name = name
        self.tuoi = tuoi
        self.nam_sinh = nam_sinh
        self.que_quan = que_quan

    def showInfor(self):
        print(self.name)
        print(self.tuoi)
        print(self.nam_sinh)
        print(self.que_quan)

sinhvienA = Student("Tran Hanh", 42, 1984, "Hưng Yen")
sinhvienA.showInfor()