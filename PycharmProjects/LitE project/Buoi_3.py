#tạo list
#ListStudents= ["Hạnh", "Hằng", "Hòa", "Hoa", "Trang"]
#in kiểu dữ liệu
#print(type(ListStudents))
# đếm số lượng
#print(len(ListStudents))
#print(ListStudents[3])
#ListStudents.append("Nhím")
#print(ListStudents)
#ListStudents.pop(1)
#print(ListStudents)
#ListStudents.remove("Nhím")
#print(ListStudents)

List_01 = [["Huân", 33, "Hải Dương"], ["Hoa", 32, "Thanh Hóa"], ["Nhím", 4, "Hải Dương"]]
print(List_01)

for x in List_01:
    for y in x:
        print(y, end = " ")
    print("xxx")


Iris_tuple = ("Iris", "S", "IS", "Cún", "Bông")
print(Iris_tuple)
print(Iris_tuple[3])

Tuple_2 = (("Huan béo", "Hải Dương", "đẹp trai"), ("Nhím thối", "Thanh Hóa", "đáng yêu"))

#List_01 = lst(Iris_tuple)


Iris_set = {0, 2, 7, 8, 8, 9, 3}
print(Iris_set)


Iris_dictionay = {"name":"Iris",
                  "tuoi":"33",
                  "que_quan":"Thanh Hoa"
                  }
print(Iris_dictionay)
print(Iris_dictionay["name"])
print(Iris_dictionay, ["tuoi"])
print(Iris_dictionay["que_quan"])

for key, value in Iris_dictionay:
    print(key)
    print(value)

List_Dictionary = [{"name":"Huan",
                    "tuoi":"33",
                    "que_quan": "Thanh Hoa"
                    },
                   { "name":"Nhims",
                     "tuoi":"4",
                     "que_quan": "Hai Duong"
                   }]

