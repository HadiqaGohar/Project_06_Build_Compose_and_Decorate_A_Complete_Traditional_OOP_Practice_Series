# 14. Aggregation

# Assignment:
# Create a class Department and a class Employee. 
# Use aggregation by having a Department object store 
# a reference to an Employee object that exists independently of it.


# Employee class
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def get_details(self):
        return f"Employee Name: {self.name}, ID: {self.emp_id}"

# Department class with aggregation
class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []  # Aggregation: references to existing Employee objects

    def add_employee(self, employee):
        self.employees.append(employee)

    def show_employees(self):
        print(f"Department: {self.name}")
        for emp in self.employees:
            print(emp.get_details())

# Create Employee objects (independent of Department)
emp1 = Employee("Hadiqa Gohar", 101)
emp2 = Employee("Tahira Rajput", 102)

# Create a Department object
dept = Department("Software Development")

# Aggregate existing employees into the department
dept.add_employee(emp1)
dept.add_employee(emp2)

# Display the department's employees
dept.show_employees()
