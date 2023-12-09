from abc import ABC,abstractmethod
from P1 import Dog
class A(ABC):
    @abstractmethod
    def m1(self):
        pass
class B(A,Dog):
    def m1(self):
        print("implemented abstract method")

objB=B()
objB.m1()
objB.sound()
