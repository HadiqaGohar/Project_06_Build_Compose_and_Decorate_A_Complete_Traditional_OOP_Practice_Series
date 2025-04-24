# 17. Class Decorators

# Assignment:
# Create a class decorator add_greeting that modifies a class to add a greet() method returning 
# "Hello from Decorator!". Apply it to a class Person.

# Class decorator
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    
    # Add greet method to the class
    cls.greet = greet
    return cls

# Apply the decorator to the Person class
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Create an object of the class
p = Person("Hadiqa")

# Call the dynamically added method
print(p.greet())  # Output: Hello from Decorator!
