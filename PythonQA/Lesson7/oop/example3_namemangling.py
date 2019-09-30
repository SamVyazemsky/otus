class Example:
    class_variable = "class_variable"  # class variable

    def __init__(self, variable):
        self.variable = variable  # instance variable, public
        self._variable = " ".join(["private", variable])  # instance variable, private
        self.__variable = " ".join(["Name mangling", variable])


Example.class_variable
example = Example("test")
example.variable
example._variable
example.__variable
example._Example__variable
