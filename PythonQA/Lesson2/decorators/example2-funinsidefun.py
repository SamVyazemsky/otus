# Example define functions inside other functions


def greet(name):
    def get_message():
        return "Hello "

    result = get_message() + name
    return result


print(greet("John"))
