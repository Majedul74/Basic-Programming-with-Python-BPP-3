# Student Grading and Performance Analysis System

## Project Title

Student Grading and Performance Analysis System

## Objective

Develop a Python application to manage student records, calculate grades, and analyze class performance using core Python concepts such as data structures, file handling, conditional statements, and loops.

## Project Tasks

1. **Data Initialization**:

   - Create a CSV file to store initial student data with the following fields:
     - Student ID
     - Name
     - Subjects (e.g., Math, English, Science)
     - Marks
     - Grade
   - Store the data in Python data structures like lists or dictionaries for processing.

2. **Student Record Management**:

   - Allow the user to:
     - Add new students with marks for each subject.
     - Update marks or details of existing students.
     - Remove a student record by their ID.

3. **Grade Calculation**:

   - Use conditional statements to calculate grades based on marks:
     - Example:
       - 90-100: A
       - 80-89: B
       - 70-79: C
       - <70: F
   - Assign grades for all students and update the dataset.

4. **Searching and Filtering**:

   - Provide the following options:
     - Search for a student by their ID or name.
     - Filter students based on grades (e.g., all students with grade "A").
     - Show a list of students who failed in any subject.

5. **User Interaction**:
   - Build a menu-driven program with the following options:
     - Add, update, or delete a student record.
     - View a class performance summary (average marks, top/low scorer, pass percentage).
     - Search and filter student records.

## Files Included

- `student_grading_system.py`: The main Python script that implements the student grading and performance analysis functionality.
- `students.csv`: A CSV file that contains initial student data.
- `README.md`: This file, providing an overview of the project.

## How to Run the Project

1. **Set Up Your Environment**:

   - Ensure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

2. **Create a Project Directory**:

   - Create a folder for your project (e.g., `StudentGradingSystem`).

3. **Add Required Files**:

   - Inside your project directory, create the following files:
     - `students.csv` (copy the content provided in the project).
     - `student_grading_system.py` (copy the content provided in the project).

4. **Run the Application**:

   - Open a terminal or command prompt.
   - Navigate to your project directory using the `cd` command.
   - Run the application using the command:
     ```bash
     python student_grading_system.py
     ```
   - If you are using Python 3 and the command above doesn't work, you might need to use:
     ```bash
     python3 student_grading_system.py
     ```

5. **Interact with the Application**:
   - Use the menu options to add, update, remove, search, filter, and view student records and performance summaries.

## Sample Queries

- Add a student with ID 6, Name "Emily Clark", Math Marks 88, English Marks 92, Science Marks 85.
- Update the marks for student ID 1.
- Search for student ID 3 or Name "Bob Johnson".
- Filter students with grade "A".
- Show students who failed in any subject.

## License

This project is open-source and available for anyone to use and modify.

## Acknowledgments

- Inspired by the need for effective student record management and performance analysis.
- 
Majedul Islam

