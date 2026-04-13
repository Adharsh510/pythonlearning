class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        if self.marks >= 90:
            return 'A'
        elif self.marks >= 75:
            return 'B'
        elif self.marks >= 60:
            return 'C'
        elif self.marks >= 50:
            return 'D'
        else:
            return 'F'
students={}    
def add_student():
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    student = Student(name, marks)
    students[name] = student

    print(f"Student {name} added Successfully")
def show_all_students():
    for name, student in students.items():
        print(f"Name: {student.name}, Marks: {student.marks}, Grade: {student.grade}")
def save_to_file():
    with open("students.txt", "w") as file:
        for name, student in students.items():
            file.write(f"{student.name},{student.marks},{student.grade}\n")
    print("Data saved to students.txt")
def menu():
    while True:
        print("\n1. Add Student")
        print("2. Show All Students")
        print("3. Save to File")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            show_all_students()
        elif choice == "3":
            save_to_file()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
menu()              