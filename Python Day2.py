print
# a=b' c=7,5
# print (a, b, c)

# temp=a #temp=7
# a=b #a=5
# b=temp #b=7

# # a=5' b=7
# print(a,b)

# EG ;2
# a=a=b #a=12
# b=a-b #b=12-7=15
# a=a-b #a=12-5=7

# print(a, b)

# id() --> used to find the memory address of the variables
# a = 7
# b = 8
# print(id(a))
# print(id(b))


# ----> keywords
# keywords are reserved words which provides special meaning to
# compiler or interpretor

import keyword
# print(keyword.kwlist)
# print(len(keyword.kwlist)
# print(type(keyword.kwlist)


# to check if the string is keyword or not
# print(keyword.iskeyword("siva")) # false

# if = 8
# print(if) # error coz if is a keyword

# !----> literals
# literals is the constant value asssigned to a variables
# A variables is considers to be constant when it is defines
# in caps

# a= 78 # is a variable
# a=78 # A constant

# hash() --> it creates a hash value for constant
# provides error for non constant datatypes
# n1=89=7j
# print(hash(n1))

# f1 =(7, 8, 9)
# print(hash(f1) error


# ! // --> floor version

# a = 765433
# b = 19
# print(a/b) # --> the out will be in integer for the output
# based on floor value

#!  ** --> used for power of a number

# ! assigment --> ==, >, <, !=, <=, >=
# a = 8
# b= 7
# print(a>b) # true

# a = 9
# b = 5
# print(a==b)

# ! bitwise operator --> &, \, ^, ~, <<, >>
# a = 7
# b = 4
# print(a&b)

# AND
# A B  A&B
# 0 0  0
# 0 1  0
# 1 0  0
# 1 1  1

# 2^4 2^3 2^2 2^1 2^0
# 8   4   2   1

# 0   1   1   1       # --> 7
# 0   1   0   0       # --> 4 &
# -----------------------
# ! logical
# and, or, not
# a = 6
# print(a>3 and a<10)
# print(a>7 or a<30)
# print(a>8 and a<10)

# ! Identify operator
# is, is not
a = 8
b = 8
print(a is b)
print(a==b)

a = [1,2,3]
b = [1,2,3]
print(a is not b)

# ! Membership operator
# in, not in
#11 = [7,8,9,0,6,5]
# num = 55
# print(num in 11)
# print(num not in 11)

# num = 678
# print(8 in num) # errror
# ! conditional statement
# IF, ELIF, ELSE

# Eg:1
#--> C syntax
# if (condition){
#     statement
#     statement
#     statement
# statement

# Eg:1
# a = 6
# if a:
#     print("hello")

# Eg:2
a = 6
if a>3:
    print("yes")
else:
    print("no")
# Eg;3
if 7>8:
    print("hello")

# print("no")

# Eg:4
# a = 0
# a = none
# a = false
# a = ""
# if a:
#     print("yes")
# else:
# print("no")

# Eg:5
a = 4
if a>2:
    print("yes")
else:
    print("no")
# a number is even or odd
n = int9input("enter the number:  ")
   if n = 42==0:
     print("n, is even")
else:
     print(n, "is odd")
 name,age,national




















