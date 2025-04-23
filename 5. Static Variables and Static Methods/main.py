# 5. Static Variables and Static Methods

# Assignment:
# Create a class MathUtils with a static method add(a, b) that returns the sum. 
# No class or instance variables should be used.

class MathUtils:

    @staticmethod
    def add(a, b):
        return a + b
    
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = MathUtils.add(num1, num2)
print(f"The sum is: {result}")    