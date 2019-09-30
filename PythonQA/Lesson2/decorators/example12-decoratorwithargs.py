def decorator(func):
    def wrapper(*args, **kwargs):
        print "args: ", args, " kwargs:", kwargs
        func(*args, **kwargs)

    return wrapper


@decorator
def f(a, b, c, platypus="Why not?", test="1"):
    print a, b, c, platypus, test


# f = decorator(f)

f("Bill", "Linus", "Stieve", platypus="Homer!", test="Hello, I'm kwargs")
