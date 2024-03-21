# ! Method ridding
# * Polymorphism in classes
class bank :
    def ratio(self):
        print("All banks has repo rate")

         
class SBI(bank):
    def ratio(self):
        print("SBI rate is 9%")


class IOB(bank):
    def ratio(self):
        print("IOB rate is 7.5%")


i = IOB()
i.ratio()


s = SBI()
s.ratio()


# ! Eg:2

class USA:
    def language(self):
        print("English")

    def capital(self):
        print("Washington DC")

class India(USA):
    def language(self):
        print("None")

    def capital(self):
         print("New delhi")

I = India()
I.language()
I.capital()


# ! Eg:3
# Polymorphism using objects

# c1, c2, --> c1 = print(c1), print(c2)
# f1, f2

class c1:
    def f1(self):
        print("class1")
        

class c2(c1):
    def f1(self):
        super().f1()
        print("class2")


obj1 = c2()
obj2 = c1()

def display(a):
    a.f1()

display(obj1)    
display(obj2)


# * changing the functionality of built in functions
class shooping:
    def __init__(self, l1):
        self.items = len(l1)
     def __len__(self):
         length = len(self.items)
         return length
    
        
s = shooping[1, 2, 3, 4, 5]()
print(len(s))

# ! method overloading
# ! eg:1
class suming:
    def add(self, a, b):
        prpint(a+b+c)

    def add(self, a, b, c):
        print(a+b+c)

s = suming()
#s.add(4, 3) # ! ----> error
s.add(4, 5, 1)



a = 9
b = 6
# print(a+b)
print(a.__add__(b))
'''
# ! Eg :2
class summing:
    def add(self, a=None, b=None, c=None):
        if a!= None and b!=None and c!=None:
            print(a+b+c)
        elif a!=None and b!=None:
            print(a+b)
        else:
            print(a)
            

obj= summing()
obj.add(2)
obj.add(3, 4)
obj.add(1,2,3)











'''
# ! --->Task

#Write the code for the below tasks using function
#!)>d1 = {"shirt": 1000, "pant"; 1500, "Shoes"; "900", "h
