class Dog:
    def __init__(self, name):
        self.name = name

dog1 = Dog("Buddy")   # <-- __init__ runs here
print(dog1.name)      # Output: Buddy
