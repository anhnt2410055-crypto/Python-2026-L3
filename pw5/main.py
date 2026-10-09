import os
import zipfile
from input import input_student
from output import display_students
from domains.student import Student

def load_data():
    students = []
    if os.path.exists("students.dat"):
        print("Found students.dat. Decompressing...")
        with zipfile.ZipFile("students.dat", "r") as zip_ref:
            zip_ref.extractall(".")

        if os.path.exists("students.txt"):
            with open("students.txt", "r", encoding="utf-8") as f:
                for line in f:
                    name = line.strip()
                    if name:
                        students.append(Student(name))

        if os.path.exists("marks.txt"):
            with open("marks.txt", "r", encoding="utf-8") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if len(parts) == 3:
                        name, mark, credit = parts
                        for s in students:
                            if s.name == name:
                                s.add_mark(float(mark), int(credit))
        print("Data loaded successfully!")
    else:
        print("No students.dat found. Starting fresh.")
    
    return students

def compress_data():
    print("Compressing data to students.dat...")
    with zipfile.ZipFile("students.dat", "w") as zip_ref:
        if os.path.exists("students.txt"):
            zip_ref.write("students.txt")
        if os.path.exists("courses.txt"):
            zip_ref.write("courses.txt")
        if os.path.exists("marks.txt"):
            zip_ref.write("marks.txt")
    print("Compression complete!")

def main():
    students = load_data()

    print("\n--- INPUT MODE ---")
    num_students = int(input("Enter number of students: "))
    for i in range(num_students):
        print(f"\nStudent {i+1}:")
        students.append(input_student())

    display_students(students)

    compress_data()

if __name__ == "__main__":
    main()