from abc import ABCMeta, abstractmethod, abstractproperty


class Movable():
    __metaclass__ = ABCMeta

    @abstractmethod
    def move(self):
        """Move object"""
        pass

    @abstractproperty
    def speed(self):
        """Speed"""


class Car(Movable):
    def __init__(self):
        self.speed = 10
        self.x = 0

    def move(self):
        self.c += self.speed

    def speed(self):
        return self.speed


assert issubclass(Car, Movable)
assert isinstance(Car(), Movable)
