# Python Day 8
# ! Eg:1
#def profile(name, age, place):
#    txt = "my name is{}, iam{}years old. iam from{}."
#    print(name, age, place)
#profile("siva", 29, "kadapa")

# Eg:2
# ? function with return statement
#def f1():
#    z = 8
#print(z)

#def gracemark():
#    c = a*b
#    return c
#f1(6, 8)
#def f1(a, b):
 #   c = a*b
#    return c
# print(f1(6, 8))
#obj = f1(6, 8)
#obj1 = f1(4, 6)

#def gracemark():
#    print(object+4)
#    print(object1+4)
#    gracemark(obj)

# ! return
# 1.) a variable declared inside thefunction can be accesed outside the fuunction
# 2.) using return
# 3.) return does not print anything
# 4.) we cannot write any code below return statement

# ? problem:1
#def palindrome(n):
#    string = str(n)
#    rev = str(n)[::_1]
#    if string==rev:
#        print(n, "palindrome")
#    else:
#        print("not palindrome")
#a = int(input("Enter the value: "))
#palindrome(a)

# ? BASED ON THE DACLARATION OF PARAMETRS AND ARGS
# ? FUNCTIONS ARE DIVIDE INTO 5 CATEGORIES

# POSITIONAL ARGS
# KEYWORD ARGS
# DEFAULT ARGS
# VARIABLE ARGS
# VARIABLE LENGTH ARGS
# KEYWORD VARIABLE LENGTH ARGS

# *POSITIONAL ARGS
# Eg:1
#def profile(name, ohone, mark):
#    txt = "my name is {}. my phone number is {}. i got {} marks."
#    print(txt.format(name, phone, mark))

#     profile(9391039214, "siva", 95)


# * keyword args
# ! Eg:1
# ? to overcome the disadvantages of podition args, we use keyboard args.
# ? it is the process of initialising the parametrs with the args while callinf=g the function

#def profile(name, phone, mark):
#    txt = "my name is {}. my phone number is {}. i got {} marks."
#    print(txt.format(name, phone, mark))

#    profile(name = "siva", phone = 9391039214, mark = 95)

# todo ---> exception of keyboard args function
#def profile(name, phone, mark):
#    txt = "my name is {}. my phone number is {}. i got {} marks."
#    print(txt.format(name, phone, mark))

#    profile(name = "siva", phone, mark)

# default args
#the method of assigning the argument to the parametr while declaring the function
# ! Eg:1]
#def profile(name, phone, mark):
#  txt = "my name is {}. my phone number is {}. i got {} marks."
#  print(txt.format(name, phone, mark))

#profile("siva", 9391039214, "kurnool")


#Problem Statement – Given a string S(input consisting) of ‘*’ and ‘#’. 
#The length of the string is variable. The task is to find the minimum number of ‘*’ 
#or ‘#’ to make it a valid string. The string is considered valid if the number of ‘*’ 
#and ‘#’ are equal. The ‘*’ and ‘#’ can be at any position in the string.
#Note : The output will be a positive or negative integer based on number of ‘*’ 
#and ‘#’ in the input string.

#(*>#): positive integer
#(#>*): negative integer
#(#=*): 0

# ! exception
#def profile(name, place = "kadapa", phone):
#    if place == "kadapa" or place == "kadapa":
#        txt = "my name is {}. my phone number is {}. iam from {}."
#        print(txt.format(name, phonr, place))
#    else:
#        print("you are not eligible to signup")
#profile{"sia", 9391039214}

# * variable lenght
#! Eg:1
#To pass more then 1 arg to a paremeter means we use variable length args
#To convert normal paremeter to variable length param, add to ther prefix of param
## name="sid", 'name2', 'name3'
# def profile(*ame):
#
#for val in name:
#
#print("My name is", val)
# profile("sid", 'name2', 'name3')

# ! Eg:2
#def profile(*name, age):
#    for val in name:
#        print("my name is val", "may age is", age)
#profile("siva", 'name2', 'name3', 22)

#def profile(*name, age):
#    for val in name:
#        print("my name is val", "may age is", age)
#profile(22,"siva", 'name2', 'name3')

# * keyword variable args
# Eg:1
#def price(price_list):
#    print(price_list)

#print(shirt = 1000, iphone = 80000)

#d1 = {"a":100, "b":200, "c":300}
#d1 = dict(a = 100, b = 200, c = 300)
#print(d1)

#n = 5
#{1:1, 2:4, 3:9, 4:16, 5:25}
#n = int(input("Enter the number: "))
##d1 = {}
#for val in range(1, n+1):
#    d1[val1] = val**2
#print(d1)

#def d1(n):
#    d1 = {}
##    for val in range(1, n+2):
#        d1[val] = val**2
#        print(d1)
#d1(5)

# ! --------> object oriented programming

# class
# objects
# inheritance
# polymorphism
# absraction
# encapsulation

# ! class is a blue print of an object

#l1 = [1, 2, 3, 4, 5, 6]

# Eg:1
#class c1:
#    name = "sri"
#    print(name1)

# Eg:2
#class c1:
#    name = "sri"

#c = person() # os object
# then process of creation of an object is called as instantiation
#print(c.name)

# ? Eg:3
#creation of a method
# when the function is crated with a class is called as method

#class Person:
 #   def display(Person):
  #      print("hello welcome to classes")

 #       p = person()
#p.display()

# ? Eg:4
# methods without paramter
#class person:
##    def display(person, name, age):
#        print(name, age)

#p = person()
#p.display("sri", 22)

# ? Eg:5
#class person:
#    name3 = "sri" # attribute or static variable

#    def display(person):
#        print(person.name3)

#p = person()
#p.display()

# ? Eg:6
#class person1:
#    fname = "sri"
#    name1 = "T"

#    def first_name(self):
##        print(self.fname)

#    def full_name(self):
#        print(self.fname+" "+self.name1)

#p = person()
#p.first_name()
#p.full_name()

# ? Eg:7
# constructors ----> __init__()
#this is a special method which has the ability to execute ios
#calling it manually through the process of instantiation
#class profile():
 #   def d1(self): # constructor method
 #3       print("hey")

##p = profile() # through this method
#p.__init__()









              














    










  


































