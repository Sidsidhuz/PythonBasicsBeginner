class Employee:
    "This is Employee class" # point 1
    employs= [] # Class variable
    raise_amt = 5
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
    @classmethod
    def increase_amt(cls,amt):
        cls.raise_amt = cls.raise_amt + amt
        return cls.raise_amt

    @classmethod
    def expand(cls,string):
        # print(len(string.split('-')))
        if len(string.split('-')) == 3:
            first,last,pay = string.split('-')
            return cls(first = first,last = last,salary= int(pay),mid = None)
        elif len(string.split('-')) == 4:
            first,mid,last,pay = string.split('-')
            return cls(first = first,mid = mid,last = last, salary =int(pay))
        else:
            return "Invalid Data !!"

emp1 = Employee('John','Smith',150000)
# emp1.increase_amt(10)
# print(emp1.raise_amt)
# print(emp1.mail)
#############################################################################
str1 = 'Ram-Kumar-10000'
str2 = 'David-Luke-30000'
str3 = 'Rahul-Shiva-40000'
str4 = 'Sam-s-joy-50000'


l1 = str1.split('-')
emp2 = Employee(first=l1[0],last=l1[1],salary=int(l1[2]))

emp3 = Employee.expand(str2)
emp4 = Employee.expand(str4)

print(emp1.fullname())
print(emp2.fullname())
print(emp3.fullname())
print(emp4.fullname())

