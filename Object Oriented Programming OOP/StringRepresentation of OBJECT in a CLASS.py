class Employee:
    def __init__(self,first,last,salary):
        self.first = first
        self.last = last
        self.mail = first.lower()+last+'@gmail.com'
        self.salary = salary
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def __str__(self): #point 1
        return self.fullname()

obj = Employee('Sid','TV',200)
obj1 = Employee('dsf','TV',200)

print(obj1)# If this statement was passed without declaring the point 1 __str__/__repr__ , this returns an object.
#Since we have declared the point 1 , the function returns the fullname and that is printed here