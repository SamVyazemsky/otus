"""
So in our example, algorithm search path is : D, B, A, C, A.
A class cannot appears twice in search path, so the final version is D, B, A, C:

    Looking in D
    If not found, looking in B
    If not found, looking un B first parent A
    If not found, going back in B others parents (none)
    If not found, looking in D others parents : C

"""


class A:
    def who_am_i(self):
        print("I am a A")


class B(A):
    def who_am_i(self):
        print("I am a B")


class C(A):
    def who_am_i(self):
        print("I am a C")


class D(B, C):
    def who_am_i(self):
        print("I am a D")


d1 = D()
d1.who_am_i()

