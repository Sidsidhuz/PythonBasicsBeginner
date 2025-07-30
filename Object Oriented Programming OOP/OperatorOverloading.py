class Employee:
    def __init__(self,first,last,salary):
        self.first = first
        self.last = last
        # self.mail = first.lower()+last+'@gmail.com'
        self.salary = salary
    @property  # this is used to convert the method into a property of the object / need not call it just self.fullname instead of self.fullname()
    def fullname(self):
        if self.first == None and self.last == None:
            return f"Object Deleted"
        return '{} {}'.format(self.first, self.last)

    @property
    def email(self):
        return f'{self.first.lower()}{self.last.lower()}@gmail.com'
    @fullname.setter
    def fullname(self,name):
        first,last = name.split()
        self.first = first
        self.last = last
    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None


    def __str__(self): #point 1
        return self.fullname

    def __add__(self1,self2):
        return self1.salary + self2.salary

    def __mul__(self1,self2):
        return self1.salary*self2.salary


obj0 = Employee('Sid','TV',200)
obj1 = Employee('joe','p',200)
obj2 = Employee('gok','u',200)
print(obj0.email)

print(obj1)# If this statement was passed without declaring the point 1 __str__/__repr__ , this returns an object.
#Since we have declared the point 1 , the function returns the fullname and that is printed here


print(obj0+obj1)
print(obj0*obj1)

class Book:
    def __init__(self,title,pages):
        self.title = title
        self.pages = pages
    def __eq__(self,other):
        return self.pages == other.pages
b1 = Book('Python Book',10)
b2 = Book('CPP Book',10)
print(b1 == b2)