# Single Inheritance
#
# class Employee:
#     def __init__(self,first,last,pay):
#         self.first = first # -------------------------------------1
#         self.last = last # ---------------------------------------2
#         self.pay = pay  # ----------------------------------------3
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
#
#
# class Department(Employee):
#     def __init__(self,first,last,pay,department):
#         super().__init__(first,last,pay)   #-----------> instead of rewriting the line 1,2,3 we can simply use this super() to access the parent class
#         self.department = department
#
#
# emp1 = Department('John','Smith',100,'Fullstack Developer')



##################################### Multiple Inheritance / Hierarchical Inheritance#####################################
# Multiple Inheritance / Hierarchical Inheritance


# class Employee:
#     raise_am = 1.06
#
#     def __init__(self, first=None, last=None, pay=None):
#         self.first = first
#         self.last = last
#         self.mail = first + last + "@gmail.com"
#         self.pay = pay
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
#
#
#
#     def raiseamt(self):
#         return self.pay * self.raise_am
#
#
# class Developer(Employee):
#     def __init__(self, first=None, last=None, pay=None, prog=None):
#         super().__init__(first, last, pay)
#         self.prog = prog
#
#
# class Manager(Employee):
#     # listDev = []
#     def __init__(self, first=None, last=None, pay=None,listDev = [None]):
#         super().__init__(first, last, pay)
#         self.listDev = listDev
#         for i in listDev:
#             if i is None:
#                 listDev.remove(None)
#
#
#     def addDev(self, dev):
#         if dev not in self.listDev:
#             self.listDev.append(dev)
#         else:
#             print('This developer already exists')
#
#     def removeDev(self, dev):
#         if dev in self.listDev:
#             self.listDev.remove(dev)
#             print(f"{dev.fullname()} has been removed")
#         else:
#             print('This developer does not exist')
#
#     def viewDev(self):
#         for dev in self.listDev:
#             print(dev.fullname())
#
#
#
# dev1 = Developer('Sidharth','T V',50000,'Python')
# dev2 = Developer('Goku','Neel',60000,'Javascript')
# dev3 = Developer('Joe','Paul',70000,'Java')
# dev4 = Developer('Rohu','Rayu',80000,'C++')
# dev5 = Developer('Daarby','Charlie',80000,'C')
# dev6 = Developer('Ammu','Kutti',80000,'Kotlin')
#
#
# manager1 = Manager('Shilin','Babe',50000)
# manager1.addDev(dev3)
# manager1.addDev(dev2)
# manager1.addDev(dev1)
#
# manager1.viewDev()

# Multi-level Inheritance / Hybrid Inheritance

class Person:
    def __init__(self, name):
        self.name = name
    def who(self):
        print(f'I am {self.name}')
class Student(Person):
    def stud_info(self):
        print(f'{self.name} is a Student')
class Employee(Person):
    def emp_info(self):
        print(f'{self.name} is an Employee')
class Intern(Student, Employee): # Hybrid Inheritance
    def intern_info(self):
        print(f'{self.name} is an Intern')

intern1 = Intern('SiD')
intern1.who()
intern1.stud_info()
intern1.emp_info()
intern1.intern_info()