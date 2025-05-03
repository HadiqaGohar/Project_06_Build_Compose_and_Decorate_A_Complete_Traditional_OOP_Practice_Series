# 🧑‍🎓 Student Grading System using `self` in Python

This Python project demonstrates how to use the `self` keyword within a class to initialize and display student details. It also includes logic to evaluate and print grades based on the student's marks, along with error handling to manage invalid user inputs.

---

## 📌 Features

* Defines a `Student` class with `name` and `marks` attributes.
* Initializes attributes using `self` inside the constructor.
* Displays student details using the `display()` method.
* Accepts user input for name and marks.
* Assigns and displays grades based on mark thresholds.
* Handles non-numeric input errors using `try-except`.

---

## 💡 Code Overview

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

try:
    name = input("Enter your name: ")
    marks = int(input("Enter your marks: "))

    student = Student(name, marks)

    if student.marks >= 95:
        print("Congratulations You got A++")
    elif student.marks >= 90:
        print("Congratulations You got A+")
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

    student.display()

except ValueError:
    print("❌ Invalid input! Please enter numeric marks.")
```

---

## 🛠️ How It Works

1. The user is prompted to enter their name and marks.
2. The `Student` class is instantiated with this data using the `self` keyword.
3. A grading system evaluates the marks and prints a congratulatory message based on the score.
4. If the user enters non-numeric marks, a `ValueError` is caught and a helpful message is shown.
5. Student details are then displayed using the `display()` method.

---

## ✅ Example Output

```
Enter your name: Hadiqa Gohar  
Enter your marks: 95  
Congratulations You got A++  
Name: Hadiqa Gohar, Marks: 95
```

```
Enter your name: Test User  
Enter your marks: abc  
❌ Invalid input! Please enter numeric marks.
```

---

## 📚 Concepts Used

* `self` keyword
* Object-Oriented Programming (OOP)
* Conditional Statements
* User Input Handling
* Error Handling with `try-except`

---

## 📁 File Structure

```
01. Using self/
│
├── main.py       # Main script with class and grading logic
└── README.md     # Project documentation
```

---

## 🧠 Author

**Hadiqa Gohar**
📧 [tasleemhadiqa76@gmail.com](mailto:tasleemhadiqa76@gmail.com)
💼 [GitHub Profile](https://github.com/hadiqagohar)
