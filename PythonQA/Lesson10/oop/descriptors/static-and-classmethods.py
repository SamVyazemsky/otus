from datetime import date as dt


class Employee:
    idCounter = 0
    # A student ID from generator
    idGenerator = (x for x in range(0xAAAAAA, 0xEEEEEE, 0xBA))

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Employee.idCounter += 1
        self.id = Employee.idGenerator.__next__()

    def say_hello(self):
        print("Hello, my name is {}".format(self.name))

    @staticmethod
    def isAdult(age):
        if age > 18:
            return True
        else:
            return False

    @classmethod
    def emp_from_year(emp_class, name, year):
        return emp_class(name, dt.today().year - year)

    def __str__(self):
        return 'Employee Name: {} and Age: {}'.format(self.name, self.age)


print(Employee.__dict__)
e1 = Employee('Dhiman', 25)
print(e1)
e2 = Employee.emp_from_year('Subhas', 1987)
print(e2)
print(Employee.isAdult(25))
print(Employee.isAdult(16))
print(e1.__dict__)

allEmployees = []  # List of employees
for number in range(25):
    newEmp = Employee("Employee-{}".format(number), number)
    allEmployees.append(newEmp)
    print(newEmp.name)
