"""
super() is in the business of delegating method calls to some class in the instance’s ancestor tree
    the method being called by super() needs to exist
        write a root class
    the caller and callee need to have a matching argument signature
        use kwargs
    and every occurrence of the method needs to use super()
"""


class Mammal(object):
    def __init__(self, mammalName):
        print(mammalName, 'is a warm-blooded animal.')

    def pr1(self):
        print("print from dog")


class Dog(Mammal):
    def __init__(self):
        print('Dog has four legs.')

    def pr(self):
        super().pr1()


d1 = Dog()
print(Dog.__mro__)
d1.pr()