class A1():
     # def who_am_i(self):
     #     print("I am a A1")
    pass


class A2():
     def who_am_i(self):
         print("I am a A2")

class A3():
     def who_am_i(self):
         print("I am a A3")


class B(A1, A2):
#     def who_am_i(self):
#         print("I am a B")
    pass


class C(A3):
    def who_am_i(self):
        print("I am a C")


class D(B,C):
#     def who_am_i(self):
#         print("I am a D")
    pass

d1 = D()
d1.who_am_i()
