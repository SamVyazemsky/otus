# Only for python 3.+


class countdown(object):
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return countdown_iter(self.start)


class countdown_iter(object):
    def __init__(self, count):
        self.count = count

    def __next__(self):
        if self.count <= 0:
            raise StopIteration
        r = self.count
        self.count -= 1
        return r


c = countdown(5)
for i in c:
    print(i, end=" ")
