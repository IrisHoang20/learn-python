# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


























print()
print()
print()

#print("Hello, World.!")

#################################
#if 5>3:
#    print("Số 5 lớn hơn số 3")

#################################
#x = 5
#y = "Hello Iris"
#print(y)
#print(x)

##################################
#x = 12
#x = "Hello Iris, i love you"
#print(x)

####################################
#x = int(3.5)
#y = str(3.56)
#z = float(8)
#print(x)
#print(y)
#print(z)

####################################
#x = 3.012
#y = 3
#z = "Love Iris"
#h = 'Hello world'

#print(type(x))
#print(type(y))
#print(type(z))
#print(type(h))

#####################################
#x = 3+5j
#y = 5j
#z = -5j

#print(type(x))
#print(type(y))
#print(type(z))

#####################################
#x = 1 #int
#y = 2.8 #float
#z = 1j #complex

#convert from int to float
#a = float(x)

#convert from float to int
#b = int(y)

#convert from int to complex
#c = complex(x)
#print(a)
#print(b)
#print(c)
#print(a, b, c)
#print(type(a))
#print(type(b))
#print(type(c))
# note: you can not convert complex number into another number type.

########################################
#import random module, and display a random number from 1 to 9

#import random
#print(random.randrange(1,10))

#######################################
#a = 'Hello'
#print(a)

######################################
# you can assign a multiline string to a variable by using three quotes '''string''' or """string"""
#a = '''hello
#my name is Iris
#what's your name???'''

#print(a)

#######################################
#square brackets can be used to access elements of the string.
#example: get the character at position 1 (remember that the first character has the position 0)

#a = 'Hello Iris'
#print(a)
#print(a[0])
#print(a[1])

#####################################
# looping through a string: since string are arrays, we can loop through the characters in a string, with a FOR loop

#for x in 'banana':
#    print(x)

######################################
# string lengh: to get the length of a string, use the len() function: the len() function returns the length of a string

#a = 'Hello, Iris. We love you'
#print(len(a))

#####################################
#to check if the certain phrase or character is present in a string, we can use the keyword IN
# Example: check if 'free' is present in the following text?

#txt = 'The best things in life are free!'
#print('free' in txt)
#print('Iris' in txt)

######################################
#to concatenate or combine 2 or more strings together we can use + operator
#a = 'Hello '
#b = 'Iris '
#c = 'How are you?'
#d = a+b+c
#print(a)
#print(b)
#print(c)
#print(d)

#to add space when concatenate 2 or more strings
#a = 'Hello'
#b = 'Nhim'
#c= 'I love you'
#d = a+b+c
#e = a+' '+b+' '+c
#print(d)
#print(e)

###########################################
#age = str(36)
#text = 'My name is Iris, I am' + ' ' + age
#print(text)

#use f-string function to combine string + number
age = 36
text = f'My name is Iris, I am {age}'
print(text)


print()
print()
print()
price = 59
text = f'The price is {price} dollars'
print(text)


#f-string: placeholder has a modifier to format the value number
print()
print()
print()
price = 59
text = f'The price is {price:.2f} dollars'
print(text)

#f-string: placeholder contain python code
print()
print()
print()
text = f'The price is {20*59} dollars'
print(text)

print()
print()
print()
a = 10
b = 5
text = f'The price is {a*b} dollars'
print(text)

###########################################
#escape character \ : use to \ to add an illegal character in the string
print()
print()
print()
text = 'we are the so-called \'Vikings\' from the north.'
print(text)

#use \ to add single quote ' character
print()
print()
print()
text = 'I\'m Iris, what\'s your name?'
print(text)

#use \ to add backslash \ character to string
print()
print()
print()
text = 'this is backslash character: \\'
print(text)

#use \n to split 1 string to multiple line
print()
print()
print()
text = 'Hello Nhím. \nHow are you? \nDo you know that i love you so much? \nYes, I always love you. \nThanks for comming to mylife'
print(text)

#use \r to remove part of string
print()
print()
print()
text = 'This is a long text but \rpart of this text will be removed'
print(text)

#use \t to insert tab character into the string
print()
print()
print()
text = 'We will use backslash \tto insert tab character to this text'
print(text)

#use \b to insert backspace character into string
print()
print()
print()
text = 'We will use backslash to insert \bbackspace to the string'
print(text)

########################################
#string methods
#1.convert the first character to upper case
print()
print()
print()
text = 'hello guys, my name is Iris'
print(text)
print(text.capitalize())

##########################################
#python booleans:
print()
print()
print()
print(10>9)
print(10==9)
print(10<9)

#use IF statement:
print()
print()
print()
a = 200
b = 33
if b > a:
    print('b is greater than a')
else:
    print('b is not greater than a')

#bool() function allows you to evaluate any value and give you True or False in return
#evaluate string and number
print()
print()
print()
print(bool('Hello'))
print(bool(15))
print(bool(['táo', 'nho', 'gạo']))

#evaluate variables:
print()
print()
print()
x = 'Hello'
y = 15
print(bool(x))
print(bool(y))

#evaluate get False if empty string or number o
print()
print()
print()
print(bool(''))
print(bool(0))

###################################
# you can execute code based on the Boolean answer of a function:
print()
print()
print()
def myFunction():
    return True
if myFunction():
    print('Yes.!')
else:
    print('No.!')

#isinstance() function:check if an object is an integer or not:
print()
print()
print()
x = 200
print(isinstance(x,int))

#############################################
#python operators:
#use + operator to adds numbers
print()
print()
print()
print(10+5)

#use - operator to minus numbers
print()
print()
print()
print(6-3)

x = 12
y = 5
print(x-y)

#use * operator for multiplication
print()
print()
print()
print(2*3)

a = 2
b = 125
print(a*b)

#use / operator for division
print()
print()
print()
print(10/2)
x = 10
y = 5
print(x/y)

#dùng phép tính % để chia lấy số dư
print()
print()
print()
print(10%3)
x = 10
y = 3
print(10%3)

#dùng ** để tính lũy thừa (số mũ)
print()
print()
print()
print(2**5)
x = 2
y = 5
print(2**5)
z = 2**5
print(z)

#dùng // để chia lấy số nguyên
print()
print()
print()
print(10//3)
x = 10
y = 3
print(x//y)
z = x//y
print(z)

#################################
#Python assignment operators: assignment operators are used to assign values to variables
# use = operator to assign value to variable
print()
print()
print()
x = 5
print(x)

#use += : để cộng 1 giá trị vào 1 biến đã được khai báo trước đó
print()
print()
print()
k = 5
k +=4  #cộng 4 vào giá trị k đã được khai báo trước đó rồi, nếu ko khai báo biến k trước đó thì sẽ lỗi
print(k)

# use -= : để trừ 1 giá trị vào 1 biến đã được khai báo trước đó.
print()
print()
print()
h = 12
h -=5
print(h)

#use *= : để nhân 1 giá trị vào 1 biến đã được khai báo trước đó rồi.
print()
print()
print()
t = 12
t *=3
print(t)

#use /= : để chia 1 biến đã được khai báo trước đó cho một giá trị nào đó
print()
print()
print()
l = 80
l /=2
print(l)

#use %= : để chia lấy dư 1 biến đã khai báo trước đó cho một gi trị
print()
print()
print()
g = 14
g %= 3
print(g)

#use //= : để chia lấy nguyên 1 biến đã khai báo trước đó với một giá trị
print()
print()
print()
s = 13
s //=3
print(s)

#use **= : để lũy thừa (mũ) 1 biến đã khai báo trước đó với 1 số
print()
print()
print()
f = 5
f **=2
print(f)

####################################
#python comparison operators






