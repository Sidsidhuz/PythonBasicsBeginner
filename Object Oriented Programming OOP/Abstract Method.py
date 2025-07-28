# Abstract Method

from abc import ABC,abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass
    @abstractmethod
    def gear_shift(self):
        pass

class Car(Vehicle):
    def Sunroof(self):
        print('Opening Sunroof .....')

    def start(self):#1
        pass

    def stop(self):#2
        pass


    def gear_shift(self):#3
        pass
# 1,2,3 and the abstract methods and all the abstract method must be declared in  the child class or else it will cause an error


class Truck(Vehicle):
    @staticmethod
    def Sunroof(self):
        print('No sunroof')

    def start(self):
        print ("Starting the Truck ....")


    def stop(self):
        print("Stoping the truck ..")
        pass

    def gear_shift(self):
        print("Shifting gear !!")
        pass

Volvo = Truck()
Volvo.start()
Volvo.stop()
Volvo.gear_shift()
Truck.Sunroof(Volvo)


