# ! ---> looping

# looping can be implemented using
# for loop
# while loop

# ! ---> for loop
# ? for loop is used for itertion, if we know the number of times the loop have to run
# ? it is used to literate the iterals eg(string, list, tuple, etc..,)

# todo --> syntax for loop

# ! for syntax in c
# for (i=0;i<10;i==){
#   print("hello");
# }

# ! for syntax in python
# for underfined_variable in range(start, end, step):
# statement
# statement
# statement

# ? Eg:1
# to print the values 1 to 10 using for loop

# for i in range(0,10): #(n,n-1)
#    print(val)

# ? Eg;2
# for val in range(1, 15, 3):
#    print(val)

# ? Eg;3
# to decrement the value

# for val in range(10, 0, -1)
    # print(val)

# for val in range(10, 0, -2)
    # print(val)

# for val in range(10, 0, 1):
#     print(val) # no output

# ? Eg:4
# ! print the output of 7th multiplication table from 21 to 43
#for val in range(21, 43+1, 7):
#     print(val*7)

# ? Eg:4
# ! print the output of 7th multiplication table from 21 to 43
# for val in range(21, 43+1, 7):
#    print(val*7)
# ? Eg:5
# ! print the output of 7th multiplication table from 21 to 43
for val in range(21, 47+1, 9):

# -- > method:2
#     print('7','*', val,'=', val*7)
#     ans="7 * {} = {}"
#    print(ans.format(val, val*7))


# ?Eg:5
# break --> used to terminate the loop

# for val in range(1, 10):
#    if val ==6:
#       break
#    print(val)

# ?Eg:5
# break --> used to terminate the loop

# for val in range(1, 1000):
#    if val ==1000000:
#        break
#    print(val)


# ? Eg:6
#for val in range(1, 10):
#    if val ==9:
#        print(val)
#        break

# ! continue statement
# Eg:1
# for val in range(1, 10):
#     if val ==8:
#         continue
#     print(val)

# ! practice probleeeeeems
# ? print the even number between 20 to 40
# for val in range(1, 30):
#     if val ==6 or val ==8 or val ==21:
#         continue
#     print(val)


# for val in range(20, 40):
#     if val ==6 or val ==10 or val ==20:
#        continue
#     print(val)

# Eg:2
# ? print the even number between 20 to 40

# for val in range(20, 40):
#     if val ==6 or val ==10 or val ==20:
#        continue
#     print(val)

# ! --------> while loop
# while is used when we do not know the number of times the lop have
# ? to iterate the non iterable element while loop is used

# todo syntax

# iniotialisation
# while condition
#     statement
#     increse or decrease

# ! Eg:1
# to iterate number from 1 to 18

 i = 0
 while i<11:
    print(i)
# Assesment
# 1.) cats and mouse: Hacker rank
#2.) Print the factorla of 8 using for loop
#3.) Write a program to display sum of odd numbers and even
# numbers that fall between
# 12 and 37(including both numbers)
#4.) Write code to print the sum of number using while loop #n1 = 123 -> 1+2+3 = 6
#5.) Prine th reverse of given number --> n1= 234 o/p --> 432















