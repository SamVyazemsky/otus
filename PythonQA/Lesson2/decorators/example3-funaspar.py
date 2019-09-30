# Example, function as param. We can sent one function to another function as parameter.


def greet(name):
    return "Hello {}".format(name)


def call_func(func):
    other_name = "John"
    return func(other_name)


print(call_func(greet))
