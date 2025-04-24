# 13. Composition

# Assignment:
# Create a class Engine and a class Car. 
# Use composition by passing an Engine object to the Car class during initialization. 
# Access a method of the Engine class via the Car class.

class Engine:
    def start(self):
        return "Engine started!"

    def stop(self):
        return "Engine stopped."

# Car class with composition
class Car:
    def __init__(self, engine):
        self.engine = engine  # Composition: Car HAS an Engine

    def start_car(self):
        return self.engine.start()

    def stop_car(self):
        return self.engine.stop()

# Create an Engine object
my_engine = Engine()

# Pass it to the Car object
my_car = Car(my_engine)

# Accessing Engine methods through Car
print(my_car.start_car())  # Output: Engine started!
print(my_car.stop_car())   # Output: Engine stopped.
