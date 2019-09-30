class Example:
    class_property = 1


e1 = Example()
e1.class_property = 2
e2 = Example()
print(Example.__dict__)
e1.some_property = True
print(e1.__dict__)  # {'some_property': True}
e1.class_property = 2
print(e1.__dict__)  # {'some_property': True, 'class_p
print(e2.__dict__)
del(e1.__dict__['class_property'])
