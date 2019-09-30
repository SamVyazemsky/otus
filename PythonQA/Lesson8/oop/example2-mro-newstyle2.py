"""
In Python 2, search path is F, A, X, Y, B.

With Python 3, search path should be : F, A, X, Y, B, Y, X and after removing « bad heads » : F, A, B, Y, X.
"""


class X():
    def who_am_i(self):
        print("I am a X")


class Y():
    def who_am_i(self):
        print("I am a Y")


class A(Y, X):
    def who_am_i(self):
        print("I am a A")


class B(Y, X):
    def who_am_i(self):
        print("I am a B")


class F(A, B):
    def who_am_i(self):
        print("I am a F")

print(F.mro())
