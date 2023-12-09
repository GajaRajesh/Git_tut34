from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
    def sound1(self):
        print("hello")

class Dog(Animal):
    def sound(self):
        print("dog sound")

d= Dog()
d.sound()
d.sound1()
