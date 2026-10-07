
from input import input_student
from output import display_students

def main():
    students = []
    
    print("--- INPUT MODE ---")
    num_students = int(input("Enter number of students: "))
    for i in range(num_students):
        print(f"\nStudent {i+1}:")
        students.append(input_student())

    display_students(students)
if __name__ == "__main__":
    main()