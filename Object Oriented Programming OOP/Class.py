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
    def __init__(self, first,last, salary = int(),mid = None):
        self.first = first
        self.last = last
        self.mail = first.lower() + last + '@gmail.com'
        self.salary = salary
        self.mid = mid

    def fullname(self):
        if self.mid is None:
            return f'{self.first} {self.last}'
        return f'{self.first} {self.mid} {self.last}'


emp1 = Employee(first='Rohit', last = 'Raju', salary=10000 )
emp2 = Employee('Rahul',mid = 'Ram',last ='RT',salary= 20000)
emp3 = Employee(first='Nandhu', last = 'Anal', salary=10000 )
print(emp1.fullname())
print(emp2.fullname(),'-->',emp3.fullname())