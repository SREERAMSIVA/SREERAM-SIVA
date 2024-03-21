#  -----> while loop
#  -----> break using while loop

# eg:1
# 1.) Iterate from 20to 30 and break the loop in 27

#i =20
#while i<31:
 #   if i ==27:
 #break
 #   print(i)
 #   i+=1

# 2.)
# =20
#while i<31:
#    print(i)
#    i+=1
#     if i ==27:
 #       break


# 3.)
#i=20
#while i<31:
 #   print(i)
 #   if i==27:
 #       break
 #   i+=1

# 4.)
#i=20
#while i<31:
 #   if i==27:
 #      print(i)
#       break
 #   i+=1


# ! ------> continue
# ----> Eg:1
#i =20
#while i<31:
#    if i==27:
#        continue
#    print(i)
#    i=i+1

# ! ----> continue
# -----> Eg:1
#i =20
#while i<31:
#    i=i+1
 #   if i==27:
 #       continue
 #   print(i)
# ! Eg:
# while to iterate from 12 to 22
# find the sum of all numbers

#i=12
#sum=0
#while i<=22:
#    sum=sum+i
#    i=i+1
#print(sum)

# ! Eg:6
# find the average of value from 20 to 25

#i=20
#sum=0
#count = 0
#while i<=25:
#    sum=sum+i
#    count+=1
#    i+=1
#print(sum/count)

# ! -------> Nested for loop
# Eg:1

#for row in range(1,3+1):
  #  for col in range(1,4+1):
 #       print(row,col)

# Eg:2
# * * * *
# * * * *
# * * * *
# * * * *


#for row in range(4):
#    for col in range(4):
#        print("* * * * *", end=" ")


#for row in range(4):
#    for vol in range(5):
#        print("*", end=" ")
#        print()


#sum = 5
#for row in range(9):
#    for col in range(5):
#        sum= sum+1
#        print(sum, end=" ")
#    print()

# ! to print stars in rights angled triangles

#for row in range(0, 6):
#    for col in range(0, row+2):
#        print("*", end=" ")
#    print()
      

#for row in range(0, 6):
#    for col in range(0, 6):
#        print("siva", end=" ")
#    print()



#for row in range(5):
#    for col in range(5):
#        if col ==0 or col ==5-1 or row ==0 or row ==5-1:
#            print("*", end=" ")
#        else:
#            print(" ", end=" ")
#    print()


# for row in range(0, 5):
#     for col in range(0, 6):
#        if ((row==0 and col==3) or (row==1 and (col>=2 and col<=4)) or (row==2 and (col>=1 and col<=5))):
#            print("*", end=" ")
#        else:
#            print(" ", end=" ")
#    print()



# ! ---> datatypes
# primary and collection datatypes
# number......like, int, float, complex
# string
# boolean
# none


# collection
# list
# tuple
# set
# dictionary


# ! list :- if the collection of elements by the surrounded by the square brackets and it is called list
# ! Eg:-
# 11 = {4, 3, 2, 3l,2, 2, ,2 ,2 ,2 }


# !. CHARACTERESTICS PF LIST
# 1. LIST HAVE TO BE SURROUNDED BY []
# 2. IT IS MUTABLE ( THE ELEMENTS IN THE LIST ARE CHANGLEBEEEELE)
# 3. EVERY ELEMENTS INSIDE LIST IS INDEXED
# 4. THE ELEMTTS INSIDE LIST WILL BE ORDERED FORMAT
# 5. IT CAN HOLD DUPLICATE VALUES
# 6. ITS HETEROGENOUS


# TO ACCESS ELEMENTS IN LIST
#11 = [1, 4, 5, 6, 7, 8, 9]
#print(11)

# --> Indexing
#              :- in the collection datatypes like, list, tuple, string, the elements willl be allowytedg with predefined unique value are called index

# we have 2 types of indexing
# positive indexing --> starts with 0 from left hand side
# negative indexing --> starts with -1 from right hand side

# ? ---> positive indexing
# list1 = [1, 4, 7, 89, 7, 7.5, "p", "i"]

# ? ------> slicing
#lst1 = [1, 4, 1, 7, 89, 7, 7.5, "p", "i"]
#print(lst1[-4:-1]
#print(lst1[-7:-1:2])
#print(lst1[-7:-1:3])

# to insert to odd element inside list

# append()
# l1 = [9, 8, 0, 6]
  



































