# 18. Property Decorators: @property, @setter, and @deleter

# Assignment:
# Create a class Product with a private attribute _price. 
# Use @property to get the price, @price.setter to update it, 
# and @price.deleter to delete it.

class Product:
    def __init__(self, price):
        self._price = price  # Private attribute by convention

    @property
    def price(self):
        print("Getting price...")
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        print("Setting price...")
        self._price = value

    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price

# Create Product object
item = Product(250)

# Access the price
print(item.price)  # Getting price... → 250

# Update the price
item.price = 300  # Setting price...
print(item.price)  # Getting price... → 300

# Delete the price
del item.price  # Deleting price...
