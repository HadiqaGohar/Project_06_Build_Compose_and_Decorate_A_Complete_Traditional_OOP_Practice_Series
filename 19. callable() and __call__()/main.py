# 19. callable() and __call__()

# Assignment:
# Create a class Multiplier with an __init__() to set a factor. 
# Define a __call__() method that multiplies an input by the factor. 
# Test it with callable() and by calling the object like a function.

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor

# Create an object with a factor
double = Multiplier(2)

# Test with callable()
print(callable(double))  # Output: True

# Call the object like a function
print(double(5))  # Output: 10
print(double(10)) # Output: 20
