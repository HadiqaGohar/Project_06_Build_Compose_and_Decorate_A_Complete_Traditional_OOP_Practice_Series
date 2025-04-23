# 8. The super() Function

# Assignment:
# Create a class Person with a constructor that sets the name. 
# Inherit a class Teacher from it, add a subject field, and use super() 
# to call the base class constructor.

class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person created: {self.name}")

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Call the constructor of the Person class
        self.subject = subject
        print(f"Teacher created: {self.name}, Subject: {self.subject}")        

# Example usage
teacher = Teacher("Arif Rozani", "Python")
teacher = Teacher("Zia Khan", "Javascript")
teacher = Teacher("Hamzah Syed", "NEXT.js")
teacher = Teacher("Ameen Alam", "Typescript")
