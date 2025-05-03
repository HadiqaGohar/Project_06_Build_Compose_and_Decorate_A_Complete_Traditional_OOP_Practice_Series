# # 1. Using self

# # Assignment:
# # Create a class Student with attributes name and marks. 
# # Use the self keyword to initialize these values via a constructor. 
# # Add a method display() that prints student details.


# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def display(self):
#         print(f"Name: {self.name}, Marks: {self.marks}")

# # Creating an instance of the Students class
# # student1 = Student("Hadiqa Gohar", 95)
# # student1.display()        

# # Using input to get student details
# student = Student(input("Enter your name: "), int(input("Enter your marks: ")))
# student.display()  # Displaying the student details

# _____________UPDATE__________________

# 1. Using self

# Assignment:
# Create a class Student with attributes name and marks. 
# Use the self keyword to initialize these values via a constructor. 
# Add a method display() that prints student details.zz


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

# Creating an instance of the Students class
# student1 = Student("Hadiqa Gohar", 95)
# student1.display()        

# Using input to get student details
student = Student(input("Enter your name: "), int(input("Enter your marks: ")))

if student.marks >= 95:
    print("Congratulations You got A++")
elif student.marks >= 90:
    print("Congratulations You got A+")   
elif student.marks >= 95:
    print("Congratulations You got A") 
elif student.marks >= 85:
    print("Congratulations You got B++") 
elif student.marks >= 80:
    print("Congratulations You got B+") 
elif student.marks >= 75:
    print("Congratulations You got B") 
elif student.marks >= 70:
    print("Congratulations You got C++") 
elif student.marks >= 65:
    print("Congratulations You got C+")
elif student.marks >= 60:
    print("Congratulations You got C") 
elif student.marks >= 55:
    print("Congratulations You got D++") 
elif student.marks >= 50:
    print("Congratulations You got D+")  
elif student.marks >= 45:
    print("Congratulations You got D+")   
else:
    print("You are failed")

student.display()  # Displaying the student details
