# Polymorphism



#method overriding
class Parent:
    def __init__(self,name,eye_color):
        self.name = name
        self.eye_color = eye_color
    def show_info(self):
        print(f"{self.name}'s eye color is: {self.eye_color}")

class Child(Parent):
    def __init__(self,name,eye_color,toyCount):
        super().__init__(name,eye_color)
        self.toyCount = toyCount
    def show_info(self):############################################### method overriding could take place here if this function is commented. If so then the show_info from the parent class will the considered in point #1
        print(f"{self.name}'s eye color is: {self.eye_color} and has {self.toyCount} toys")



obj1 = Child("A",'blue',10)
obj2 = Parent("B","green")
obj1.show_info()#--------------------------------------------------point1
obj2.show_info()

