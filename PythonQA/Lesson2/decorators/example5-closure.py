# Example of closure. Inner functions have access to the enclosing scope


def compose_greet_func(name):
    def get_message():
        return "Hello there, {}!".format(name)

    return get_message


greet = compose_greet_func("John")
print(greet())
