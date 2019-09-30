# First example


def tags(tag_name):
    def tags_decorator(func):
        def func_wrapper(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))
        return func_wrapper
    return tags_decorator


@tags("p")
def get_text(name):
    return "Hello " + name


print(get_text("John"))

# Another example


# def decorator_maker(decorator_arg1, decorator_arg2):
#     print "Decorator make args:", decorator_arg1, decorator_arg2
#
#     def decorator(func):
#         print "Decorator args:", decorator_arg1, decorator_arg2
#
#         def wrapper(*args, **kwargs):
#             print "Wrapper args:", args, kwargs
#             return func(*args, **kwargs)
#
#         return wrapper
#
#     return decorator
#
#
# @decorator_maker("Tesla", "SpaceX")
# def f(arg1, arg2):
#     print "Function args:", arg1, arg2
