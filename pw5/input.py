from domains.student import Student

def input_student():
    name = input("Enter student name: ")
    student = Student(name)

    with open("students.txt", "a", encoding="utf-8") as f:
        f.write(f"{name}\n")

    num_marks = int(input(f"How many courses for {name}? "))
    for i in range(num_marks):
        print(f"  Course {i+1}:")
        mark = float(input("    Enter mark: "))
        credit = int(input("    Enter credit: "))
        student.add_mark(mark, credit)

        with open("courses.txt", "a", encoding="utf-8") as f:
            f.write(f"{credit}\n")

        with open("marks.txt", "a", encoding="utf-8") as f:
            f.write(f"{name},{mark},{credit}\n")

    return student