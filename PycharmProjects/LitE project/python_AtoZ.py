print('Hello, World.!')

##############Python Variables#################

"""Lesson: in python, variables are created when you assign a value to it"""
print()
print()
print()
x = 5
y = 'Hello Iris'
z = 9.15
k = ['táo', 'nho', 'cam']
l = {'nho', 'ổi', 'xoài'}
print(x)
print(type(x))
print(y)
print(type(y))
print(z)
print(type(z))
print(k)
print(type(k))
print(l)
print(type(l))


"""Lesson: ÉP KIỂU: là cách để định dạng dữ liệu cho biến bất kỳ"""
print()
print()
print()
x = str(3)
y = int(3)
z = float(3)
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))

"""TYPE() function: you can get the data type of a variable with type() function"""

"""CASE SENSITIVE: variable names are case sensitive: nghĩa là phân biệt chữ hoa - chữ thường, ví dụ A, a là 2 biến khác nhau"""
print()
print()
print()
a = 3
A = 'I love you, Iris'
print(a)
print(A)
print(type(a))
print(type(A))

"""Assign multiple values to multiple variables: có thể assign nhiều value cho nhiều biến trên cùng 1 dòng"""
print()
print()
print()
x, y, z, t = 'Orange', 3, 'Cherry', 10.25
print(x)
print(y)
print(z)
print(t)
print(type(x))
print(type(y))
print(type(z))
print(type(t))

"""Assign one value to multiple variables: có thể assign cùng 1 giá trị cho nhiều biến khác nhau"""
print()
print()
print()
x = y = z = 'Orange'
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))

"""UNPACK COLLECTION: if you have list, tuple then python allows you to extract the values into variables"""
print()
print()
print()
list = ['táo', 'nho', 'cam', 'bưởi', 'đào']
x, y, z, m, n = list
print(x)
print(type(x))
print(y)
print(z)
print(m)
print(n)
print(list)
print(type(list))


"""output variables: PRINT() function
+ PRINT(x): in giá trị 1 biến
+ PRINT(x, y, z): in giá trị nhiều biến cùng 1 lúc
+ PRINT(x+y+z): in kết quả của phép tính"""
print()
print()
print()
x = 'Python is awesome'
print(x)

a = 'Python'
b = 'is'
c = 'awesome'
print(a,b,c)
print(a+b+c)
print(a + ' ' + b + ' ' + c)

print(5+3)


"""GLOBAL VARIABLES
global variables are created outside of a function, can be used by everyone both inside & outside of function."""
#Sample_01: create a global variable and use it inside the function

print()
print()
print()
x = 'awesome'
def function():
    print('Python is '+x)
function()

"""" biến trong và ngoài trùng nhau: trong function sử dụng giá trị biến trong, ngoài function sử dụng giá trị biến ngoài """
print()
print()
print()
x = 'awesome'

def funct():
    x = 'fantastic'
    print('Python is '+ x)   #trong function sử dụng biến trong, hiển thị : Python is fantastic
funct()

print('Python is '+x)   # ngoài function sử dụng biến ngoài, hiển thị: Python is awesome


"""GLOBAL keyword: để đưa 1 biến từ local thành biến global"""
#biến tạo trong function là biến local, chỉ sử dụng được trong function, tuy nhiên có thể đưa biến này thành GLOBAL bằng keyword global như ví dụ sau
print()
print()
print()
def funct():
    global h
    h = 'fantastic'
    print('Iris is '+h)   # gọi biến local
funct()
print('Python is '+h)    # gọi biến global sau khi chuyển biến local thành global, nếu ko thì sẽ bị lỗi


"""GLOBAL keyword: chuyển 1 local biến thành 1 global biến để thay thế global biến cùng tên x đã khai báo trước đó"""
print()
print()
print()
x = 'I love '

def funct():
    global x
    x = 'My name is '

funct()

print(x + 'Iris')


#####################PYTHON DATA TYPE##########################
print()
print()
print()
x = 'Iris'  #type:string
print(x)
print(type(x))

y = 3       #type:int
print(y)
print(type(y))

z = 3.14   #type:float
print(z)
print(type(z))

m = 1j     #type: complex
print(m)
print(type(m))

n = ['Nhím', 'Voi', 'Gấu']    #type:list
print(n)
print(type(n))

u = ('Táo', 'Nho', 'Cam', 'Xoài')     #type:tuple
print(u)
print(type(u))

r = range(6,14,2)    #type:range
print(r[2])
print(type(r))

p = {'name': 'Iris', 'age': '33', 'sex' : 'Female'}  #type:dictionary
print(p)
print(type(p))

w = {'hổ', 'voi', 'sư tử'}   #type:set
print(w)
print(type(w))

e = frozenset({'cam', 'đào', 'ổi'})    #type:frozenset
print(e)
print(type(e))

g = True     #type:bool
print(g)
print(type(g))

q = b'Hello'    #type:bytes
print(q)
print(type(q))

a = bytearray(5)   #type:bytearray
print(a)
print(type(a))

b = memoryview(bytes(5))   #type:memoryview
print(b)
print(type(b))

w = None
print(w)
print(type(w))    #type:NoneType


#################PYTHON NUMBERS####################
"""there are 3 numeric types in Python: int; float; complex"""
#RANDOM() function: to make a random number
print()
print()
print()

import random
print(random.randrange(1,20))


#####################PYTHON STRING####################
"""strings are also arrays"""
print()
print()
print()
a = 'Hello Iris, I love you'
print(a)
print(a[0])

"""looping through a string"""
print()
print()
print()
b = 'banana'
for x in b:
    print(x)
print(b)

"""string length"""
print()
print()
print()
a = 'Hello Iris, I love you so much'
print(a)
print(len(a))

"""IN keyword: to check if a certain phrase or character is present in a string"""
#sample: check if 'free' is present IN the following text:
print()
print()
print()
text = 'The best things in life are free!'
print('free' in text)
print('Iris' in text)

#the sample above with IF statement:
print()
print()
print()
text = 'The best things in life are free!'
x = 'Iris'
if x in text:
    print('Yes! ' + x + ' is in the text')
else:
    print('No! ' + x + ' is not in the text')

"""NOT IN keyword: check if phrase or character is not present in a string"""""
print()
print()
print()
text = 'The best things in life are free!'
print('Iris' not in text)

#use IF in above sample:
print()
print()
print()
text = 'The best things in life are free!'
x = 'expensive'
if x not in text:
    print(x + ' is not in string')
else:
    print(x + ' is in the string')

"""Slicing strings: để cắt ký tự, đoạn text ra khỏi string"""
#sample: cắt ký tự thứ 6-9 (tương đương chữ Nhím) trong đoạn text sau
print()
print()
print()
text = 'Hello Nhím, I love you so much'
print(len(text))
print(text[6:10])
print(text[:10])
print(text[2:])
print(text[-5:-2])  #use nagative indexing

"""BIẾN ĐÔI STRING"""
#chuyển viết thường sang viết hoa
print()
print()
print()
text = 'xin chào việt nam'
print(text)
print(text.upper())

#chuyển viết hoa sang viết thường
print()
print()
print()
text = 'TÔI LÀ NGƯỜI VIỆT NAM'
print(text)
print(text.lower())

#xóa ký tự trống (space) thừa ở đầu và cuối string
print()
print()
print()
text = '           Hà Nội mùa này vắng những cơn mưa     '
print(text)
print(text.strip())

#Replace string: thay đổi ký tự/một phần trong string
print()
print()
print()
text = 'Hello Việt Nam'
print(text)
print(text.replace("Hello", "Xin chào"))

#Split string: cắt string thành danh sách list dựa vào ký tự đặt ra
print()
print()
print()
text = 'Hello, My name is Iris. I am learning Python'
print(text)
print(text.split(" "))  #cắt text thành các từ đơn bằng dấu space
print(text.split("."))  #cắt text thành các từ đơn bằng dấu .

#String concatenation: ghép string bằng dấu +
print()
print()
print()
text_1 = 'Hello'
text_2 = 'My name is IRIS'
text_3 = 'I love you'
print(text_1 + " " + text_2 + " " + text_3)

"""F-string: có thể kết hợp string và số bằng f-string"""
print()
print()
print()
age = 33
text = f'My name is Iris, I am {age}'
print(text)

"""F-string: placeholder có format kiểu dữ liệu: kết hợp string + số (trong đó có định dạng số """
print()
print()
print()
price = 150
text = f'The price is {price} dollars'   #ko định dạng cho số
print(text)

text_01 = f'The price is {price:.2f} dollars'  #định dạng price là số thập phân có 2 số sau dấu .
print(text_01)

"""F-string: placeholder là kết quả 1 phép toán"""
print()
print()
print()
text = f'Tổng của 3 & 4 là {3+4}'
print(text)
x = 12
y = 5
text_00 = f'Hiệu của x và y là {x-y}'
print('Số x là: ', x)
print('Số y là: ' , y)
print(text_00)


"""Cách thêm các ký tự không hợp lệ vào trong string: 
trong Python có một vài ký tự ko hợp lệ nếu thêm vào string, nhưng bằng cách chèn \ trước ký tự ko hợp lệ thì có thể thêm ký tự đó vào string một cách bình thường"""
print()
print()
print()

# chèn kí tự '
print('My name is Iris, I\'m 33 years old')

#chèn kí tự \
print('Đây là cách chèn ký tự \\ vào trong text')

"""CÁC HÀM CHUYỂN ĐỔI STRING"""
#capitalize() : viết hoa ký tự đầu tiên
print()
print()
print()
text = 'tên tôi là iris'
print(text.capitalize())

#casefold() : chuyển string sang viết thường
text = 'MY NAME IS IRIS'
print(text.casefold())

#count(): đếm số lần xuất hiện của một ký tự nào đó
text = 'hàm đếm số lần xuất hiện của ký tự trong chuỗi'
print(text.count())




