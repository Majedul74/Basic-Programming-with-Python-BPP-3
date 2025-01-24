import csv

# Constants for grade calculation
GRADE_THRESHOLDS = {
    'A': (90, 100),
    'B': (80, 89),
    'C': (70, 79),
    'F': (0, 69)
}

# Function to read student data from CSV
def read_students_from_csv(filename):
    students = []
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append(row)
    return students

# Function to write student data to CSV
def write_students_to_csv(filename, students):
    with open(filename, mode='w', newline='') as file:
        fieldnames = ['Student ID', 'Name', 'Math', 'English', 'Science', 'Marks', 'Grade']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for student in students:
            writer.writerow(student)

# Function to calculate grades
def calculate_grade(marks):
    for grade, (low, high) in GRADE_THRESHOLDS.items():
        if low <= marks <= high:
            return grade
    return 'F'

# Function to add a new student
def add_student(students):
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    math = int(input("Enter Math Marks: "))
    english = int(input("Enter English Marks: "))
    science = int(input("Enter Science Marks: "))
    marks = (math + english + science) / 3
    grade = calculate_grade(marks)
    students.append({
        'Student ID': student_id,
        'Name': name,
        'Math': math,
        'English': english,
        'Science': science,
        'Marks': marks,
        'Grade': grade
    })
    write_students_to_csv('students.csv', students)

# Function to update a student record
def update_student(students):
    student_id = input("Enter Student ID to update: ")
    for student in students:
        if student['Student ID'] == student_id:
            student['Name'] = input("Enter new Name: ")
            student['Math'] = int(input("Enter new Math Marks: "))
            student['English'] = int(input("Enter new English Marks: "))
            student['Science'] = int(input("Enter new Science Marks: "))
            student['Marks'] = (student['Math'] + student['English'] + student['Science']) / 3
            student['Grade'] = calculate_grade(student['Marks'])
            write_students_to_csv('students.csv', students)
            print("Student record updated.")
            return
    print("Student ID not found.")

# Function to remove a student record
def remove_student(students):
    student_id = input("Enter Student ID to remove: ")
    for student in students:
        if student['Student ID'] == student_id:
            students.remove(student)
            write_students_to_csv('students.csv', students)
            print("Student record removed.")
            return
    print("Student ID not found.")

# Function to search for a student
def search_student(students):
    search_term = input("Enter Student ID or Name to search: ")
    for student in students:
        if student['Student ID'] == search_term or student['Name'].lower() == search_term.lower():
            print(student)
            return
    print("Student not found.")

# Function to filter students by grade
def filter_students_by_grade(students):
    grade = input("Enter grade to filter (A, B, C, F): ")
    filtered_students = [student for student in students if student['Grade'] == grade]
    for student in filtered_students:
        print(student)

# Function to show students who failed
def show_failed_students(students):
    failed_students = [student for student in students if student['Math'] < 70 or student['English'] < 70 or student['Science'] < 70]
    for student in failed_students:
        print(student)

# Function to view class performance summary
def class_performance_summary(students):
    total_marks = sum(float(student['Marks']) for student in students)
    average_marks = total_marks / len(students) if students else 0
    top_scorer = max(students, key=lambda x: float(x['Marks']), default=None)
    low_scorer = min(students, key=lambda x: float(x['Marks']), default=None)
    pass_percentage = (len([s for s in students if s['Grade'] != 'F']) / len(students)) * 100 if students else 0

    print(f"Average Marks: {average_marks:.2f}")
    print(f"Top Scorer: {top_scorer['Name']} with {top_scorer['Marks']} marks" if top_scorer else "No students found.")
    print(f"Lowest Scorer: {low_scorer['Name']} with {low_scorer['Marks']} marks" if low_scorer else "No students found.")
    print(f"Pass Percentage: {pass_percentage:.2f}%")

# Main menu function
def main_menu():
    students = read_students_from_csv('students.csv')
    while True:
        print("\nMenu:")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Remove Student")
        print("4. Search Student")
        print("5. Filter Students by Grade")
        print("6. Show Failed Students")
        print("7. Class Performance Summary")
        print("8. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_student(students)
        elif choice == '2':
            update_student(students)
        elif choice == '3':
            remove_student(students)
        elif choice == '4':
            search_student(students)
        elif choice == '5':
            filter_students_by_grade(students)
        elif choice == '6':
            show_failed_students(students)
        elif choice == '7':
            class_performance_summary(students)
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu() 