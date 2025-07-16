# Object Oriented Programming
# Class

#basic class
# class employee:
#     pass
# emp1 = employee()
# # print(emp)
# emp1.firstname = 'sid'
# emp1.lastname = 'TV'
# emp1.salary = 20000
# emp1.mail = 'sid@gmail.com'
# print(emp1.firstname)
# print(emp1.lastname)
# print(emp1.salary)
#######################################################################################

# class Employee:
#     def __init__(self,first,last,salary):
#         self.first = first
#         self.last = last
#         self.mail = first.lower()+last+'@gmail.com'
#         self.salary = salary
#
#
# emp1 = Employee('Sidharth','tv','1000000')
# print(emp1.first)
# print(emp1.mail)
####################################################################################


class Employee:
    "This is Employee class" # point 1
    p = 0
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


emp1 = Employee(first='Rohit', last = 'Raju', salary=10000 ) # Here emp1 is the object/instance of the class Employee
emp2 = Employee('Rahul',mid = 'Ram',last ='RT',salary= 20000)
emp3 = Employee(first='Nandhu', last = 'Anil', salary=10000 )
emp4 = Employee(first='Joe', last = 'Paul', salary=10000 )
print(Employee.__doc__) ##this is used to print the point 1
# for i in Employee.employs:
#     print(i.fullname())
##################################################################################################
print(emp1.incSal(4))
print(emp1.fullname(),':₹',emp1.salary)
##################################################################################################
print(emp4.__dict__) # __dict__ shows the properties and values of the instance (as a dictionary)
print(vars(emp4)) #  Result is same as __dict__


v = vars(emp2)
print(list(v.values())) # Convert the values of the instance into a list

