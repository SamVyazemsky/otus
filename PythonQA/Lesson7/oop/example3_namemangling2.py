class ManglingTest:
    def __init__(self):
        self.__mangled = 'hello'

    def get_mangled(self):
        return self.__mangled


ManglingTest().get_mangled()
ManglingTest().__mangled


class MangledMethod:
    def __method(self):
        return 42

    def call_it(self):
        return self.__method()


MangledMethod().__method()
MangledMethod().call_it()
