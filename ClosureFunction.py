#           Closure Methods

# def outer():
#     msg = 'hello' # Once the outer is invoked, this variable will be available to its sub function ---- 1
#     def inner():
#         print(msg)
#     return inner
#
# val = outer() # Val store or call the inner function indirectly --> As fucntion outer() returns inner()
# val()         # now when val is invoked the inner() it inturn call the inner function()

########################################################################################################################

def add():
    count = 0
    def increment():
        nonlocal count
        count += 5
        return count
    return increment

val = add()
print(val())
