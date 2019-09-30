class C(object):
    def foo(self):
        pass


print(C.foo) # C.__dict__['foo'].__get__(None, C)
print(C.__dict__['foo'])
c = C()
print(c.foo) # c.__getattribute__() -> C.__dict__['foo'].__get__(c, C)
print(c.foo(), C.foo(c))
