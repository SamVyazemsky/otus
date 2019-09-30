class ComparableMixin(object):
    """This class has methods which use `<=` and `==`,
    but this class does NOT implement those methods."""
    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return self <= other and (self != other)

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return self == other or self > other


class Integer(ComparableMixin):
    def __init__(self, i):
        self.i = i

    def __le__(self, other):
        return self.i <= other.i

    def __eq__(self, other):
        return self.i == other.i


assert Integer(0) < Integer(1)
assert Integer(0) != Integer(1)
assert Integer(1) > Integer(0)
assert Integer(1) >= Integer(1)

# It is possible to instantiate a mixin:
o = ComparableMixin()
# but one of its methods raise an exception:
#o != o
