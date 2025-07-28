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