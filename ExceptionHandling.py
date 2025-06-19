t = 1
while t:

    try:
        print("Division")
        a = int(input("Enter element a :"))
        b = int(input("Enter element b :"))
        res = a/b
        print(res)
        t = 0
    except(ZeroDivisionError,IndexError):
        print("ZeroDivisionError or IndexError")
        pass
    except :
        print("Unexpected error")

# def div():
#     a = int(input("Enter element a :"))
#     b = int(input("Enter element b :"))
#     res = a / b
#     print(res)
# try :
#     div()
# except :
#     print("Division error!! Try Again")
