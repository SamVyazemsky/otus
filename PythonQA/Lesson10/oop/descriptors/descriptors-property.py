class Descriptor:
    def __get__(self, obj, type):
        print("getter used")

    def __set__(self, obj, val):
        print("setter used")

    def __delete__(self, obj):
        print("deleter used")


class MyClass:
    prop = Descriptor()


# class MyClass:
#
#     def _getter(self):
#         print("getter used")
#
#     def _setter(self, val):
#         print("setter used")
#
#     def _deleter(self):
#         print("deleter used")
#
#     prop = property(_getter, _setter, _deleter, "doc string")

m = MyClass()
m.prop          # getter used
m.prop = 1      # setter used
del(m.prop)     # deleter used
