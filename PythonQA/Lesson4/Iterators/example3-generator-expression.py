b = (2*x for x in range(20))
type(b)
b.__next__()
for i in b:
    print(b, end=' ')
