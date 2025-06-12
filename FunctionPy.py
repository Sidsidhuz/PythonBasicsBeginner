#
# def Greeting(s):
#     print(f"Hello {s}")
#
# n = input("Enter your name: ")
# Greeting(n)

# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# def div(a,b):
#     return a/b
#
# print(add(1,2))
# print(sub(1,2))
# print(mul(1,2))
# print(div(1,2))

# def sqr():
#     i = 1
#     l = []
#     while i <= 10:
#         l.append(i ** 2)
#         i += 1
#     print(l)
# sqr()


def avg():
    c = int(input("Enter the count of numbers: "))
    l = 0
    for i in range(c):
        val = int(input("Enter the number: "))
        l += val
    print(f"Average ={l/c}")

avg()
