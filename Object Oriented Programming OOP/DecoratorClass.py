from datetime import time


# def decorator_function(original_function):
#     def wrapper_function():
#         print(f"Wrapper executed before{original_function._name_}")
#         return original_function()
#     return wrapper_function
# def display():
#     print("This is display function")

# wrapped=decorator_function(display)
# print(wrapped._name_)
# wrapped()

# def decorator_function(original_function):
#     def wrapper_function():
#         print(f"Wrapper executed before{original_function._name_}")
#         return original_function()
#     return wrapper_function

# @decorator_function
# def display():
#     print("This is display function")

# display()

# def decorator_function(original_function):
#     def wrapper_function(args ,*kwargs)  :####(name,age)
#         print(f"Wrapper executed before{original_function._name_}")
#         return original_function(args ,*kwargs  )###(name,age)
#     return wrapper_function
#
# @decorator_function
# def display_info(name ,age):
#     print(f"display_info with arguments:{name},{age}")
#
# display_info(name="Devin" ,age=29)
#
# class decorator_class:
#     def _init_(self ,org_function):
#         self.org_function =org_function
#
#     def _call_(self ,args ,*kwds):
#         print(f"method will call before the{self.org_function}")
#         return self.org_function()
#     def call_me(self):
#         return "hello"
#
# @decorator_class
# def display():
#     print("This is display function")
#
# display()
#
# print(display.call_me())
# print(isinstance(display ,decorator_class))
#
# import time
# def find_sqr(val):
#     start =time.time()
#     ls =[]
#     for i in val:
#         ls.append( i *i)
#     end =time.time()
#     print(f"time:-{str((end -start ) *1000)}")
#     return ls
#
# array =range(1 ,10001)
# find_sqr(array)

# import time
# def find_time(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         cal = func(*args, **kwargs)
#         end = time.time()
#         print(f'{func.__name__} took {str((end - start)*1000)} ')
#         return cal
#     return wrapper
#
# @find_time
# def find_sqr(val):
#     ls = []
#     for i in val:
#         ls.append(i**2)
#     return ls
# arry = [i for i in range(100000)]
# find_sqr(arry)

def decorator_with_argument(message):
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            print(f'{message} before calling {func.__name__}')
            result = func(*args, **kwargs)
            print(f'{message} after calling {func.__name__}')
            return result
        return wrapper
    return actual_decorator
@decorator_with_argument('hello')
def hello(name):
    print(f'Hello, {name}')


hello('SiD')