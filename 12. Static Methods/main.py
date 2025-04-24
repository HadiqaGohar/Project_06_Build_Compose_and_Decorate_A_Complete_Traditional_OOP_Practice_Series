# 12. Static Methods
# Assignment:
# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) 
# that returns the Fahrenheit value.

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

# Example usage:
while True:
    temp = input("Enter temperature in Celsius (or 'exit' to quit): ")
    if temp.lower() == "exit":
        print("❄️ Goodbye!")
        break
    try:
        celsius = float(temp)
        fahrenheit = TemperatureConverter.celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is equal to {fahrenheit:.2f}°F\n")
    except ValueError:
        print("⚠️ Please enter a valid number!\n")
