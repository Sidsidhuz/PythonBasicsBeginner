# first = "John"
# last = "Smith"
#
# print(f"{first} [{last}] is a coder")
#
# v1 = "have a great day"
# v2 = "It's Sunday"
#
# #print(f"It's a {v1[7:]} \ngreat {v2[5:]}")
#
# print(v2[:5] + v1[-9:])
# print(v1[-9:-4] + v2[-7:])
#
# l = [1,2,3,4,5]
# l.extend([6,7,8,9])
# l.pop(0)
# print(l)
#
# #
# from traceback import print_list

# s = []
# print(s.isEmpty())

#remove duplicate values from the list conserving the order of the list
# value = [12,24,35,24,88,120,155,88,120,155]
# l = []
# for i in value:
#      if i not in l:
#          l.append(i)
# print(l)

# val = [12,24,35,24,88,120,155,88,120,155]
# for i in range(len(val)):
#     j = i+1
#     while j < len(val):
#         if val[i] == val[j]:
#             val.pop(j)
#         else:
#             j+=1
# print(val)

#count the number of Lowercase and Uppercase in a given string
# String = input("Enter a string: ")
# UCount = 0
# LCount = 0
# for char in String:
#     if char.isupper():
#         UCount += 1
#     elif char.islower():
#         LCount += 1
# print(f"LOWER CASE: {LCount}")
# print(f"UPPER CASE: {UCount}")

# number = [501,12,75,150,180,145,525,50]
# l = []
# for i in number:
#     if i > 500:
#         break
#     elif i > 150:
#         continue
#     elif i % 5 == 0:
#         l.append(i)
# print(l)


# l = []
# for i in range(1,5):
#     l.append('x'*i)
# print(l)

# s = int(input("Enter an integer: "))
# string = str(s)
# ns = string[::-1]
# print(ns)

# s = int(input("Enter an integer: "))
# f = []
#
# while s != 0:
#     f.append(s % 10)
#     s = (s // 10)
# print(f)

# ls = ['red','black','blue']
# for i in range(len(ls)):
#     print(i,':',ls[i])
#
# for i,j in enumerate(ls):  # enumerate method
#     print(f'{i}:{j}')


#function Composition
# def add(x):
#     return x+2
# def mul(x):
#     return x*2
# # print(add(mul(3)))
# import random,time
#
# tickets = []
# for i in range(7):
#     tickets.append(random.randint(1,10))
# print("Be Patient")
# print("Decision Pending", end="")
# for i in range(random.randint(1,10)):
#     print(".", end = "",flush = False)
#     time.sleep(1)
# win = ''
# for i in tickets:
#     win = win + str(i)
#
# print("\n",win)

################---->Comprehension<------############################################

# val = [[1,2,3],[4,5,6],['a','b']]
# l = [val[i][0] for i in range(len(val))]
# print(l)
#
# a = [1,2,3,4]
# b = [10,20,30,40]
# l = [i+j for i,j in zip(a,b)]
# print(l)
#
#
# mat = [[1,2],[3,4],[5,6],[7,8]]
# l = [[row[i] for row in mat] for i in range(len(mat[0]))]
# print(l)

# strs = 'Devin123'
# l =tuple(i for i in strs if i.isdigit())
# print(l)

# my_list = ['tool','23',3.4,'bar',55,'toolbar']
# l = [i for i in my_list if str(i).isalpha()]
# print(l)


# def Printnum(a):
#     l = []
#     while a != 0 :
#         print(a)
#         a = a - 1
# def recNum(a):
#     if a == 0:
#         print(0)
#     else:
#         print(a)
#         return recNum(a-1)
# recNum(5)


# numbers = [3,8,1,7,9,5,4,2,10]
# temp = []
# for i in range (len(numbers)):
#     for j in range(len(numbers)):
#         if numbers[j] > numbers[i]:
#             temp = numbers[j]
#             numbers[i] = numbers[j]
#             numbers[j] = temp
# print(numbers)
# print(f"Greatest number from the list is {numbers[-1]}")
# #
# large = 0
# for i in range(len(numbers)):
#     if numbers[i] > large:
#         large = numbers[i]
#         pos = i
# print(f"largest element from the list is {large} and position is {pos}")


#################################### File Handling ####################################################################

#
# with open('2.txt','w') as f:
#     f.write('this is the appended line : 1\n')
#     f.write('this is the appended line : 2\n')
# with open('2.txt','r') as f:
#     l = f.readlines()
#     l1 = []
#     for i in l:
#
#         l1.append(i.strip())
# print(l1)
# # print(l)
#
# with open('2.txt','w') as f:
#     f.write('this is the appended line : 1\n')
#     f.write('this is the appended line : 2\n')
# with open('2.txt','r') as f:
#     l = f.readlines()
#     l1 = []
#     for i in l:
#
#         l1.append(i[5:8])
# print(l1)
# # print(l)

# with open('2.txt','r+') as f:
#     f.write('this is the appended line : 1\n')
#     f.write('this is the appended line : 2\n')
#     f.write('this is the appended line : 3\n')
#     f.write('this is the appended line : 4\n')
#     f.write('this is the appended line : 5\n')
#     f.write('this is the appended line : 6\n')
#     f.seek(0)
#     print(f.read())


# with open('2.txt','r') as f:
#     print(f.readline())
#     print(f.tell())
#     print(f.readline())
#     print(f.readline())
#     f.seek(0)
#     print(f.readline())

# with open(r'G:\Pythoneering\Exptlab1\WorkOutExpt\maxresdefault.jpg','rb') as f:
#     PicBi = f.read()
# with open(r'G:\Pythoneering\Exptlab1\WorkOutExpt\maxresdefault.jpg','rb') as f, open('NewEnd.jpg', 'wb') as new:
#     new.write(f.read())
#######################################################################################################################
# [(1,'odd'),(2,'even'),(3,'odd'),(4,'even'),(5,'odd')]
# l = [(i ,'even') if i % 2 == 0 else (i,'odd') for i in range(1,6)]
# print(l)

# number = [-2,-3,-1,0,1,2,3,0,5]
# #['-ve','-ve','-ve','zero','+ve','+ve','+ve','zero','+ve']
# l = ['-ve' if i < 0 else 'zero' if i==0 else'+ve' for i in number]
# print(l)

##################################################################################################################

# [['Apple', 'Banana', 'Cherry'], ['Date', 'Fig', 'Grape'], ['Kiwi', 'Lemon', 'Mango']]
# [['Apple'], ['Banana'], ['Cherry'], ['Date'], ['Fig'], ['Grape'], ['Kiwi'], ['Lemon'], ['Mango']]

# mat = [['apple','banana','cherry'],
#        ['date','fig','grape'],
#        ['kiwi','lemon','mango']]
#
# l = [[i.capitalize() for i in j] for j in mat ]
# print(l)
# li = [[j.capitalize()] for i in mat for j in i ]
# print(li)
########################################################################################################################
# input --> [1, 14, 24, 12, 113]
# expected output
# ['child', 'teen', 'adult', 'child', 'adult']

# c = int(input("enter the number of people: "))
# lis = [int(input("enter the ages :"))for j in range(c) ]
# l = ['child' if i <= 13 else 'teen' if 13 < i < 20 else 'adult' for i in lis]
# print(lis)
# print(l)
########################################################################################################################
# Track the number of students using a class variable
# class Student():
#     c_std = []
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.c_std.append(name)
#     def count(self):
#         return len(self.c_std)
#
#
#
# std1 = Student("Sidharth", 21)
# std2 = Student("Joe", 20)
# std3 = Student("Gokul", 23)
#
# print(len(Student.c_std))
################################################################################################################
# Class for Bank Account that supports
# deposit
#withdraw
#checkBalance

# class Bank:
#     accounts = []
#     def __init__(self,name,amount = 0):
#         self.name = name
#         self.amount = amount
#         self.accounts.append(name)
#
#     def CheckBalance(self): #balance
#         return self.amount
#
#     def Withdraw(self,amountwith):
#         if amountwith > self.amount:
#             print("Insufficient Balance")
#         else:
#             self.deposit -= amountwith
#
#     def deposit(self,amountdep):
#         self.amount += amountdep
#         print(f"Successfully Deposited amount: {amountdep}")
#         print(f"Current amount: {self.amount}")
#
#
#     def adminPanal(password):
#         if password == "@123":
#             print("Admin Login Successfull ")
#             print("Press 1 to view registered people ")
#             print("Press 2 to exit ")
#             i = input()
#             if i == "1":
#                 print("People are :",end='')
#                 print(Bank.accounts)
#             elif i == "2":
#                 return
#
#         else:
#             print("Admin Login Failed")
#
# per1 = Bank("Sidharth",2000)
# per2 = Bank("Gokul",5000)
# per3 = Bank("Joe",6000)
# per4 = Bank("Abhi sheik",7000)
# per5 = Bank("Chinjitha",8000)
#
# # print(per1.CheckBalance())
# # per1.Withdraw(12000)
# # print(per1.CheckBalance())
# # per1.deposit(20000)
# # print(per1.CheckBalance())
# Bank.adminPanal("@123")
########################################################################################################################
# File Handling using Re
# Extract the phone number from the give file using re method
# import re
# with open('data.txt','r+') as f:
#     lines = f.readlines()
#     strSamp = ''
#     for i in lines:
#         strSamp += i
#     # print(strSamp)
#     pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
#     matches = pattern.finditer(strSamp)
#     for match in matches:
#         # print(match.group())
#         # print(type(match))
#         with open ('dataEntry.txt','a+') as E:
#             E.write(match.group())
#             E.write('\n')
#
#
#
######################ENCAPSULATION#############################
################Q1###############################
# class Person:
#     def __init__(self, first, age):
#         self.first = first
#         self.__age = age
#
#     def display(self):
#         return f'Name: {self.first},Age:{self.__age}'
#
#     def get_age(self):
#         return self.__age
#
#     def set_age(self, age):
#         if age > 0 :
#             self.__age = age
#
#         else:
#             print('Age cant be zero')
#
# per1 = Person(first='A', age=20)
# per2 = Person(first="B", age=30)
# per1.set_age(32)
# print(per1.display())
####################################Q2########################################################

# class ATM:
#     def __init__(self, balance):
#         self.__balance = balance
#
#     def withdraw(self,amount):
#         if self.__check_balance(amount):
#             self.__balance -= amount
#             print(f'Withdraw {amount}')
#         else:
#             print('Insufficient balance')
#
#
#     def __check_balance(self,amount):
#         if self.__balance <= amount:
#             return self.__balance>= amount
#
#
# atm = ATM(100)
# atm.withdraw(200)

##########################################Q3###########################################################################

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.__grade = grade

    def result(self):
        avg = self.__calculate_avg()
        print(f"{self.name}'s average grade is {avg}")
        print("Result" , 'Pass' if avg >=60 else 'Fail')
    def __calculate_avg(self):
        return sum(self.__grade) / len(self.__grade)

s1 = Student('John', [40,40,64,80,74])
s1.result()
s2 = Student('Sid', [100,100,100,100,10])
s2.result()
