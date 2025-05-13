#x, y, z = 'Apple', 'Banana', 'Orange'
#print(x)
#print(y)
#print(z)
from sys import is_finalizing

#a = b = c = 'Fruits'
#print(a)
#print(b)
#print(c)


#fruit = ['táo ', 'nho ', 'bưởi ']
#x, y, z = fruit
#print(x)
#print(y)
#print(z)

#print(x, y, z)
#print(x+y+z)

#a = 5
#b = 7
#print(a+b)
#print(5+7)

#x = 'Awesome'
#def myfunc():
#    x = 'Fun'
#    print('Python is ' +x)
#myfunc()
#print('Pyton is '+x)


#def myfunc():
#    global x
#    x = 'Great.!'
#    print('Python is '+x)
#myfunc()
#print('Iris is '+x)

#x = 'awesome'
#def myfunc():
#    global x
#    x = 'fun'
#    print(x)
#myfunc()
#print(x)

###################################
#to check if a certain phrase or character is present in a string, we can use keyword IN
#Example: check if 'free' is present in the following text:
#text = 'The best things in life are free!'
#print('free' in text)
#print('Iris' in text)

#use IF statement:
#text = 'The best things in life are free!'
#if 'free' in text:
#    print("Yes, 'free' is present.")

#check NOT IN
#text = 'The best things in life are free!'
#print("IRIS" not in text)

#check IF NOT IN
#text = 'The best things in life are free!'
#if "Iris" not in text:
#    print("Iris is not in this text.!")

############################################
#slicing strings
#example: get the characters from position 2 to position 5
#b = 'Hello Iris'
#print(b[2])
#print(b[0:5])

#slice from the start: get the characters from the start to position 5
#b = 'Hello Iris, I love you'
#print(b[:7])

#slice to the end: get the characters from position 2 and all the way to the end:
#b = 'This is my beautiful baby girl'
#print(b[4:])

#nagative indexing:
#b = 'Hello, World!'
#print(b[-5:-2])
#print(b[8:11])

#upper case: the UPPER() method returns the string in upper case:
a = 'hello iris, how are you?'
print(a)
print(a.upper())

#lower case: the LOWER() method returns the string in lower case:
a = 'I LOVE YOU SO MUCH NHÍM THỐI'
print(a)
print(a.lower())

#remove whitespace: the STRIP() method removes any whitespace from the beginning or the end:
print()
print()
print()
a = '     Hello, do you know that      I love you so much       '
print(a)
print(a.strip())


#replace string: the REPLACE() method replaces a string with another string:
print()
print()
print()
a = 'Hello Iris, I love you so much'
print(a)
print(a.replace("H", "K"))

#split string: the SPLIT() method returns a list where the text between the specified separator becomes the list items
print()
print()
print()
a = 'Hello, Iris , Nhím!'
print(a.split(","))

############################################
#python list
print()
print()
print()
my_list = ['Táo', 'Chuối', 'Dưa', 'Nho']
print(my_list)

#use len() function để check độ dài của list (số phần tử trong list)
print()
print()
print()
list =['sách', 'vở', 'bút', 'chì', 'tẩy', 'vở']
print(list)
print(len(list))

#use type() check datatype của list
print()
print()
print()
list = ['Nhím', 4, 'Iris', 33, 'Huân béo', 32]
print(list)
print(len(list))
print(type(list))

# use list() constructor to make a list
print()
print()
print()
list_02 = ['Na', 'Táo', 'Nho', 'Bưởi']
list_01 = (('Iris', 'Emily', 'Jason', 'Venus', 'Pedro'))
print(list_01)
print(list_02)
print(len(list_01))
print(len(list_02))
print(type(list_01))
print(type(list_02))

################################
#access list items
print()
print()
print()
list = ['ngô', 'khoai', 'sắn', 'thóc', 'lúa']
print(list)
print(list[0])
print(list[1])
print(list[2])
print(list[3])
print(list[4])

#negative indexing
print()
print()
print()
list = ['Nhím', 'Gấu', 'Bơ', 'Khoai']
print(list[-1])
print(list[-2])
print(list[-3])

#return the range
print()
print()
print()
list = ['táo', 'nho', 'cam', 'quýt', 'mít', 'dừa']
print(list[0:3])
print(list[:3])
print(list[2:])
print(list[-4:-2])

#use IF: để check sự hiện diện của 1 item ở trong list
print()
print()
print()
list = ['máy tính', 'chuột', 'bàn phím', 'dây nối', 'máy sấy tóc']
if 'chuột' in list:
    print('có \'chuột\' nằm trong danh sách này')

###############################
#change item value in list
print()
print()
print()
list = ['táo', 'nho', 'cam', 'bưởi', 'xoài']
print(list)
list[1] = 'ngô'
print(list)
print(len(list))
print(type(list))

#change the range of item values
print()
print()
print()
list = ['điện thoại', 'máy tính', 'laptop', 'ipad', 'chuột', 'bàn phím']
print(list)
list[1:3] = ['táo', 'ngô']
print(list)

#insert new item to the list










#######################################
#python IF...ELSE
print()
print()
print()
a = 330
b = 200
if a > b:
    print('a lớn hơn b')
else:
    print('a nhỏ hơn b')

#python IF...ELIF
print()
print()
print()
a = 20
b = 200
if a > b:
    print('a lớn hơn b')
elif a == b:
    print('a bằng b')
else:
    print('a nhỏ hơn b')

#short hand IF
print()
print()
print()
a = 100
b = 20
if a > b:
    print('a lớn hơn b')

#short hand IF...ELSE
print()
print()
print()
a = 10
b = 20
print('a lớn hơn b') if a > b else print('b lớn hơn a')

#short hand IF...ELIF...ELSE
print()
print()
print()
a = 10
b = 20
print('a lớn hơn b') if a > b else print('a bằng b') if a==b else print('a nhỏ hơn b')

#dùng AND để kết hợp điều kiện
print()
print()
print()
a = 200
b = 33
c = 500
if a > b and c > a:
    print('c > a > b')
else:
    print('chưa xác định')

# dùng OR để kết hợp điều kiện
print()
print()
print()
a = 200
b = 33
c = 500
if a > b or a > c:
    print('số a lớn hơn một trong 2 số b, c')

# dùng NOT để xác định điều kiện
print()
print()
print()
a = 33
b = 200
if not a > b:
    print('a không lớn hơn b')

#nested IF: you can have if statements inside if statements, this is called nested if statements.
print()
print()
print()
x = 41
if x > 10:
    print('x lớn hơn 10')
    if x > 20:
        print('x lớn hơn 20')
    else:
        print('không lớn hơn 20')

#the PASS statement: for some reason have an IF statement with no content, put in the PASS statement to avoid getting an error
print()
print()
print()
a = 33
b = 200
if b > a:
    pass

#############################################
#python FOR loops

#FOR loops: looping through a LIST
print()
print()
print()
fruits = ['táo', 'nho', 'đào', 'bưởi', 'cam']
for x in fruits:
    print(x)
print(fruits)

# FOR loops: looping through a STRING
print()
print()
print()
for x in 'banana':
    print(x)

text = 'I love Iris'
print(text)
for x in text:
    print(x)

# FOR loops: BREAK statement: with break statement we can stop the loop before it has looped through all the items
print()
print()
print()
fruits = ['táo', 'nho', 'cam', 'bưởi', 'xoài']
for x in fruits:
    print(x)
    if x == 'cam':
        break

#BREAK statement: exit the loop before print the last item
print()
print()
print()
fruits = ['táo', 'nho', 'cam', 'quýt', 'bưởi', 'xoài']
for x in fruits:
    if x == 'cam':
        break
    print(x)

#CONTINUE statement: to stop with the value match with if condition:
print()
print()
print()
fruits = ['táo', 'nho', 'cam', 'quýt', 'mít', 'dừa']
for x in fruits:
    if x == 'nho':
        continue
    print(x)

#RANG() function in FOR loop:
# the range() function returns a sequene of numbers, starting from 0 and increments by 1 and ends at a specified number.
print()
print()
print()
for x in range(6):
    print(x)

print()
print()
print()
for x in range(2,12):
    print(x)

print()
print()
print()
for x in range(10):
    if x == 7:
        break
    print(x)

#RANGE() function: to specify the increment value
print()
print()
print()
for x in range(2,15,2):
    print(x)

############################
#ELSE in FOR loop : the ELSE in FOR loop to spefify a block of code to be excuted when the loop is finished
print()
print()
print()
for x in range(6):
    print(x)
    print('Đây là số', x)
else:
    print('kết thúc chương trình.!')

#Noted: the ELSE block will NOT be executed if the loop is stopped by a break statement
print()
print()
print()
for x in range(6):
    if x == 3:
        break
    print('Đây là số', x)
else:
    print('kết thúc chương trình khi gặp số 3')

############################################
#NESTED LOOPS:
# a nested loop is a loop inside a loop: the inner loop will be executed one time for each iteration of the outer loop
print()
print()
print()
color = ['xanh', 'đỏ', 'tím', 'vàng']
size = ['S', 'M', 'L']
for x in color:
    for y in size:
        print(x,y)
        print('áo đồng phục nữ có màu',x,'và size',y)

#the PASS statement:
print()
print()
print()
for x in [0,1,2]:
    pass


###########################################
#python WHILE loops: with WHILE loop we can execute a set of statements as long as a condition is TRUE
print()
print()
print()
i = 1
while i < 6:
    print(i)
    i +=1    #noted: remember to increment i, or else the loop will continue forever.

# the BREAK statement: with the BREAK statement we can stop the loop even if the while condition is TRUE
#example: exit the loop when i =  3
print()
print()
print()
i = 1
while i < 6:
    print(i)
    if i==3:
        break
    i +=1

# the CONTINUE statement: để bỏ giá trị khớp với điều kiện IF và tiếp tục với vòng lặp WHILE cho đến khi kết thúc
print()
print()
print()
i = 0
while i < 6:
    i +=1
    if i==3:
       continue
    print(i)

# the ELSE statement: with ELSE statement we can run a block of code once when the condition no longer is TRUE
print()
print()
print()
i = 1
while i < 6:
    print(i)
    i +=1
else:
    print('i is no longer less than 6')

###############################################################
#PYTHON FUNCTIONS
print()
print()
print()
def function():  #cách khai báo 1 function
    print('Đây là 1 function')
function()       #cách gọi 1 function


#FUNCTION() with 1 arguments
print()
print()
print()
def function(first_name):
    print(first_name + ' Hoang')
function('Iris')
function('Ryan')
function('Alex')

#FUNCTION() with more than one arguments
print()
print()
print()
def function(first_name, last_name):
    print(first_name + " " + last_name)
function('Iris', 'Hoang')












