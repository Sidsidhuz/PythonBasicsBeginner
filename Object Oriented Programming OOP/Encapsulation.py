# Encapsulation

class Person:
    def __init__(self, first, age,salary):
        self.first = first # here first is a public variable. It can be accessed from any point in the code
        self._age = age  # _age is a protected variable in '_' is used to indicate that this variable should be used within the class & subclass only. This is a strong convention ,that is it could be used other that the class
        self.__salary = salary # '__' indicates that the variable is completely private and can only access within the class only --> Encapsulation

    def get_sal(self): #  A method has to be declared in order to access the private variable
        return self.__salary

per1 = Person(first=100, age=20, salary=100)
print(per1.first)
print(per1._age) # It is not encouraged to access protected variables outside the class
# print(per1.__salary) # this creates error --> 'Person' object has no attribute '__salary' as the __salary is a private variable
print(per1.get_sal())