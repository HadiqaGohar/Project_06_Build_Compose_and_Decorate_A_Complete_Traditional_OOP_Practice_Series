# 7. Access Modifiers: Public, Private, and Protected

# Assignment:
# Create a class Employee with:

# a public variable name,
# a protected variable _salary, and
# a private variable __ssn.
# Try accessing all three variables from an object of the class and document what happens.

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name         # Public variable
        self._salary = salary    # Protected variable
        self.__ssn = ssn         # Private variable

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self._salary}")
        print(f"SSN: {self.__ssn}")

# Create an object of Employee class
emp = Employee("John Doe", 150000, "123-45-6789")


# Without error handling this code runs fine because python allows access to protected and private variables
# but it is not a good practice to access them directly

print("____________________ \n")

# Accessing public variable (works fine)
print(f"Employee Name: {emp.name}")

# Accessing protected variable (works but should be avoided as it's convention)
print(f"Employee Salary: {emp._salary}")

# Accessing private variable (throws an error)
try:
    print(f"Employee SSN: {emp.__ssn}")
except AttributeError as e:
    print(f"Error: {e}")


print("____________________ \n")


# Using a method to access the private variable (this is allowed)
emp.display_info()

print("____________________ \n")