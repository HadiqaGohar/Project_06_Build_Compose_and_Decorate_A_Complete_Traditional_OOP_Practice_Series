# 6. Constructors and Destructors

# Assignment:
# Create a class Logger that prints a message when an object is created 
# (constructor) and another message when it is destroyed (destructor).

class Logger:
    def __init__(self):
        print("Logger created: Constructor called.")

    def __del__(self):
        print("Logger destroyed: Destructor called.")

# Creating an object
log = Logger()

# Optional: Delete the object manually (just for demo)
del log

# Or let Python automatically call destructor when program ends
