class Employee:
    def __init__(self,first,last,salary):
        self.first = first
        self.last = last
        self.mail = first.lower()+last+'@gmail.com'
        self.salary = salary
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def __str__(self):
        return self.fullname()

obj = Employee('Sid','TV',200)
obj1 = Employee('dsf','TV',200)

print(obj1)