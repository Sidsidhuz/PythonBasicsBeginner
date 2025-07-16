class Employee:
    "This is Employee class" # point 1
    employs= [] # Class variable
    def __init__(self, first,last, salary = int(),mid = None): # __init__ is used to declare Constructor  & self is used to refer the object that is called
        self.first = first
        self.last = last
        self.mail = first.lower() + last + '@gmail.com'
        self.salary = salary
        self.mid = mid
        self.employs.append(self) # employs is a list declared within the class. Any operation in the class variable should have self.

    def fullname(self): # method to show fullnames
        if self.mid is None:
            return f'{self.first} {self.last}'
        return f'{self.first} {self.mid} {self.last}'

    def incSal(self,percentage): # method used to increase salary of an employee in the class
                self.salary = (self.salary * (percentage)/100) + self.salary
                return self.salary