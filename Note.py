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


numbers = [3,8,1,7,9,5,4,2,10]
temp = []
for i in range (len(numbers)):
    for j in range(len(numbers)):
        if numbers[j] > numbers[i]:
            temp = numbers[j]
            numbers[i] = numbers[j]
            numbers[j] = temp
print(numbers)
print(f"Greatest number from the list is {numbers[-1]}")
#
# large = 0
# for i in range(len(numbers)):
#     if numbers[i] > large:
#         large = numbers[i]
#         pos = i
# print(f"largest element from the list is {large} and position is {pos}")
