# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
    #print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


name = "Iris Hoang"
age = "33"
birth_date = "20/02/1993"
sex = "male"
print(name)
print(age)
print(birth_date)
print(sex)


x = 3.1
y = int(4.321)
z = 3
name = "Iris Hoang"
print(x)
print(y)
print(z)
print(name)

print(type(x))
print(type(y))
print(type(z))
print(type(name))


a = 25
b = 6

print(f"giá trị của {a}*{b} là: {a*b}")
print(a-b)
print(a+b)
print(a/b)

#lấy phần nguyên
print(a//b)

# lấy phần dư
print(a%b)




a = 5
b = 5
if (a!=b):
    print(" a khác b")
else:
    print("a bằng b")




strA = "a khác b" if (a!=b) else "a bằng b"
print(strA)


x = 2
y = '2'
print(x)
print(y)

if(x is y):
    print("x bằng y")
else:
    print("x khác y")



z = [1,2,3,4,5,6,7,8]
for x in z:
    print(x)
    print ("next")


for x in range(0,10):
    print(x)
    print("next")

for x in range(0,10,3):
    print(x)
    print("next")



#for x in range(0,10):
#   name = input("xin mời nhập tên: ")
#  print(name)
# print("next")

# bài 1:
#name = "bài tập 01"
#print(name)
#so_nguyen = input("xin mời nhập một số nguyên: ")
#if (a%2 == 0):
#   print("bạn vừa nhập số chẵn")
#else:
#   print("bạn vừa nhập số lẻ")



#bài 2:
#name = "bài tập 02"
#print(name)
#a = int(input("xin mời nhập số nguyên a: "))
#b = int(input("xin mời nhập số nguyên b: "))
#if (a>b):
#    print("a lớn hơn b")
#elif (a==b):
#    print("a bằng b")
#else:
#    print("a nhỏ hơn b")




#bài 3:
#name = "bài tập 03"
#print(name)
#for x in range (1,6):
#    diem = float(input("Xin mời nhập điểm trung bình môn của 5 bạn: "))
#    if (diem>=8.5):
#        print("Học sinh xuất sắc")
#    elif (diem >=7.0):
#        print("Học sinh giỏi")
#    elif (diem >= 5.0):
#        print("Học sinh trung bình")
#    else:
#        print("Học sinh yếu")

#Bài 6: Kiểm tra số âm, dương hay bằng o
#name = "Bài tập 06"
#print(name)
#nhap_so = int(input('Xin mời nhập số bất kì: '))
#if nhap_so > 0:
#    print('Đây là số dương')
#elif nhap_so == 0:
#    print('Đây là số 0')
#else:
#    print('Đây là số âm')











#Bài 4: KIỂM TRA NĂM NHUẬN
#name = "bài tập 04"
#print(name)
#year = int(input('Xin mời nhập năm: '))
#if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
#    print('Đây là năm nhuận')
#else:
#    print('Ko phải năm nhuận')


#Bài 5: MÁY TÍNH ĐƠN GIẢN
#ame = "bài tập 05"
#rint(name)
# = input('Xin mời nhập a: ')
# = input('Xin mời nhập b:')
#= input("Xin mời nhập phép tính: ")
#et_qua =


#Bài 6: VẼ TAM GIÁC SỐ
#name = "Bài tập 06"
#print(name)
#n = int(input('Mời nhập số N')
#for i in range (1, n+1)
#    for j in range (1, i+1):
#        print(j, end = ' ')
#    print("")



#Bài 8: Tìm số đảo ngược
name = "Bài tập 08"
print(name)
text = str(input("Xin mời nhập chuỗi: "))
reversed_text = ""
for char in text:
    reversed_text = char + reversed_text
print("Số ban đầu là:", text)
print("Số đảo ngược là: ", reversed_text)