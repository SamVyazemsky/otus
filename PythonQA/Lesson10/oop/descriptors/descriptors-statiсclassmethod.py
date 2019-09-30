class StaticAndClassMethodHolder:

    def _method(*args):
        print("_method called with ", args)
    static = staticmethod(_method)
    cls = classmethod(_method)


s = StaticAndClassMethodHolder()
s._method()     # _method called with (<__main__.StaticAndClassMethodHolder object at ...>,)
s.static()      # _method called with ()
s.cls()         # _method called with (<class '__main__.StaticAndClassMethodHolder'>,)
