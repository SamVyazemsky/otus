# Example functions generating other functions. Function can return other function


def compose_greet_func():
    def get_message():
        return "Hello there!"

    return get_message


greet = compose_greet_func()
print(greet())
