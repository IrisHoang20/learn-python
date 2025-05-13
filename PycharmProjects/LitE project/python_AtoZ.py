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

