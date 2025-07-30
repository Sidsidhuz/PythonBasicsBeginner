# Encapsulation

class Person:
    def __init__(self, first, age,salary):
        self.first = first # here first is a public variable. It can be accessed from any point in the code
        self._age = age  # _age is a protected variable in '_' is used to indicate that this variable should be used within the class only. This is a strong convention ,that is it could be used other that the class
        self.__salary = salary # '__' indicates that the variable is completely private and can only access within the class only --> Encapsulation
