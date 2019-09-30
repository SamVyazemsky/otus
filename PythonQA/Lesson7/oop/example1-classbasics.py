class Dog:
    pass
    # # Class Attribute
    # species = 'mammal'
    #
    # # Initializer / Instance Attributes
    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age
    #
    # # instance method
    # def description(self):
    #     return "{} is {} years old".format(self.name, self.age)


print(Dog())
# <__main__.Dog object at 0x1004ccc90>
a = Dog()
b = Dog()
print(a == b)
# False
