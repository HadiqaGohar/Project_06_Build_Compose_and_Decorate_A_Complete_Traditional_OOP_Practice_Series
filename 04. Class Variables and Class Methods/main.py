# 4. Class Variables and Class Methods

# Assignment:
# Create a class Bank with a class variable bank_name. 
# Add a class method change_bank_name(cls, name) that allows changing the bank name. 
# Show that it affects all instances.

class Bank:
    bank_name = "National Bank"  # class variable

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

# print(f"Initial bank name: {Bank.bank_name}")
# new_name = "Global Bank"
# Bank.change_bank_name(new_name)
# print(f"Updated bank name: {Bank.bank_name}")        

# Access before change
print(f"Initial bank name: {Bank.bank_name}")

# Change bank name
new_name = input("Enter the new bank name: ")
Bank.change_bank_name(new_name)

# Access after change
print(f"Updated bank name: {Bank.bank_name}")
