from domains.student import Student

def input_student():
    name = input("Enter student name: ")
    student = Student(name)
    
    num_marks = int(input(f"How many courses for {name}? "))
    for i in range(num_marks):
        print(f"Course {i+1}:")
        mark = float(input("  Enter mark: "))
        credit = int(input("  Enter credit: "))
        student.add_mark(mark, credit)
        
    return student