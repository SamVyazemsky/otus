# Python 2.7
x = iter([1, 2, 3])
print(dir(x))
print(x)
print(x.next())
print(x.next())
print(x.next())
print(x.next())


# Python 3.6
x = iter([1, 2, 3])
print(dir(x))
print(x)
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
