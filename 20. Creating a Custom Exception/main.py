# 20. Creating a Custom Exception
# Assignment:
# Create a custom exception InvalidAgeError. 
# Write a function check_age(age) that raises this exception if age < 18. 
# Handle it with try...except.

# Custom Exception
class InvalidAgeError(Exception):
    def __init__(self, message="Age must be 18 or above."):
        self.message = message
        super().__init__(self.message)

# Function to check age
def check_age(age):
    if age < 18:
        raise InvalidAgeError(f"Invalid age: {age}. Must be 18 or older.")
    else:
        print("Access granted!")

# Test the function
try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except InvalidAgeError as e:
    print("Caught an exception:", e)
