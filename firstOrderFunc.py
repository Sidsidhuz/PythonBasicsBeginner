# First Order function
# handling function as a variable

# def samp(name):
#     return f"HELLO {name}"
# def demo(func,name):
#     return func(name)
# print(demo(samp,'sid'))

##########################################################################################
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y

ls = [add,sub,mul]
for i in ls:
    print(i(10,5))