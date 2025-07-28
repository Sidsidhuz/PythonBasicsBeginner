# isinstance method basically check whether the passed object belongs to the mentioned class
# this method returns True if the condition is satisfied else it returns False

# val = isinstance(1,int) # 1 is the object and
# print(val)

class Employee:
    raise_am = 1.06

    print('Parent class')

class Developer(Employee):
    print("dev child of employee")

class Manager(Employee):
    # listDev = []
   print('Man child of employee')


print(isinstance(Developer, Employee))
print(isinstance(Developer, Manager))
print(isinstance(Manager, Employee))

print(isinstance(Manager, Developer))
print(issubclass(Manager, Employee))
print(issubclass( Developer, Employee))