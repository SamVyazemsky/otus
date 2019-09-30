# In Python, methods are functions that expect their first parameter to be a reference to the current object.

# def p_decorate(func):
#
#    def func_wrapper(self):
#        return "<p>{0}</p>".format(func(self))
#    return func_wrapper
#
#
# class Person(object):
#     def __init__(self):
#         self.name = "John"
#         self.family = "Doe"
#
#     @p_decorate
#     def get_fullname(self):
#         return self.name + " " + self.family
#
#
# my_person = Person()
# print(my_person.get_fullname())

# The same but with *args and **kwargs


def p_decorate(func):
   def func_wrapper(*args, **kwargs):
       return "<p>{0}</p>".format(func(*args, **kwargs))
   return func_wrapper


class Person(object):
    def __init__(self):
        self.name = "John"
        self.family = "Doe"

    @p_decorate
    def get_fullname(self):
        return self.name+" "+self.family


my_person = Person()

print(my_person.get_fullname())

