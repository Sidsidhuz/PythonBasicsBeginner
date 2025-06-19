try:
    a = int(input("Enter element a :"))
    b = int(input("Enter element b :"))
    res = a/b
    print(res)

except:
    print("b should be non 0 element")
    pass
finally:
    print("HAI")