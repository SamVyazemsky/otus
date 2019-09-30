# Example function as variable


def greet(name):
    return "hello " + name


greet_someone = greet
print(greet_someone("John"))
