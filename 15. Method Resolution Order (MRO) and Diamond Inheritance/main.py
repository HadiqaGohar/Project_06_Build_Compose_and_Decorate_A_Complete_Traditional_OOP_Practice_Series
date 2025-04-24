# 15. Method Resolution Order (MRO) and Diamond Inheritance

# Assignment:

# Create four classes:
# A with a method show(),
# B and C that inherit from A and override show(),
# D that inherits from both B and C.
# Create an object of D and call show() to observe MRO.

class A:
    def show(self):
        print("Show from class A")

class B(A):
    def show(self):
        print("Show from class B")

class C(A):
    def show(self):
        print("Show from class C")

class D(B, C):  # D inherits from both B and C
    pass

# Create object of class D
d = D()

# Call the show method
d.show()

# Print MRO
print("Method Resolution Order:", [cls.__name__ for cls in D.__mro__])
