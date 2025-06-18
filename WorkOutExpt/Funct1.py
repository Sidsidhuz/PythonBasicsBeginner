def avg():
    c = int(input("Enter the count of numbers: "))
    l = 0
    for i in range(c):
        val = int(input("Enter the number: "))
        l += val
    print(f"Average ={l/c}")

def sqr():
    i = 1
    l = []
    while i <= 10:
        l.append(i ** 2)
        i += 1
    print(l)

