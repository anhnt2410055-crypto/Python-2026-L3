import os

def display_students(students):  
    os.system('cls' if os.name == 'nt' else 'clear')
    

    students_sorted = sorted(students, key=lambda s: s.calculate_gpa(), reverse=True)

    print("     STUDENT MARK MANAGEMENT SYSTEM     ") 
    
    for s in students_sorted:
        print(f"Name: {s.name.ljust(10)} | GPA: {s.calculate_gpa():.2f}")
        
    print("========================================")
    input("Press Enter to exit...")