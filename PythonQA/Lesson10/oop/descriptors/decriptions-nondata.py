class NonDataDesc:

    def __get__(self, obj, cls):
        print("Trying to access from {0} class {1}".format(obj, cls))


class NonDataHolder:
    non_data = NonDataDesc()


n = NonDataHolder()

NonDataHolder.non_data  # Trying to access from None class <class '__main__.NonDataHolder'>
n.non_data              # Trying to access from <__main__.NonDataHolder object at ...> class <class '__main__.NonDataHolder'>
n.non_data = 1
n.non_data              # 1
n.__dict__              # {'non_data': 1}