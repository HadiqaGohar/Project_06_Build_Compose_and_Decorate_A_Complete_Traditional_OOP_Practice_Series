# 3. Public Variables and Methods
# Assignment:
# Create a class Car with a public variable brand and a public method start().
#  Instantiate the class and access both from outside the class.

class Car:
    def __init__(self, brand):
        self.brand = brand      # Public Variable

    # Start Method

    def Start(self):
        print(f"{self.brand} is starting...")

# # Creating an object
# my_car = Car("Toyota")

# # Accessing public variable
# print("Car Brand:", my_car.brand)

# # Accessing public method
# my_car.start()        


my_car = Car(input("Enter the car brand: "))
print("Car Brand:", my_car.brand)
my_car.Start()