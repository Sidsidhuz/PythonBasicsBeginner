# program to remove all special character from a string
k = str()
s = input("enter a string :")
for i in s:
    if i.isalnum():
        k = k + i
print(k)