students = []
course = []

def add_students():
    for _ in range(int(input("enter number of students"))):
        students.append({
            'id': input("enter student id"),
            'name': input("enter student name"),
            'DoB': input("enter date of birth")  
        })  
def add_course():
    for _ in range(int(input("enter number of course")))  :
        course.append({
            'id': input("enter course id "),
            'name': input("enter course name ")
        }) 
        
def input_marks():
    cid = input("Enter course ID to input marks: ")
    course = next((c for c in courses if c['id'] == cid), None)
    
def list_course():
    print("\n--- Course List ---")
    for c in courses: 
        print(f"ID: {c['id']} | Name: {c['name']}")

def list_students():
    print("\n--- Student List ---")
    for s in students: 
        print(f"ID: {s['id']} | Name: {s['name']} | DoB: {s['dob']}")

def show_marks():
    cid = input("Enter course ID to view marks: ")
    course = next((c for c in courses if c['id'] == cid), None)
    if not course:
        print("Course not found!")
        return
    print(f"\n--- Marks for {course['name']} ---")
    for s in students:
        mark = course['marks'].get(s['id'], 'Not entered')
        print(f"ID: {s['id']} | Name: {s['name']} | Mark: {mark}")
        
while True:
    print("\n1. Add Students | 2. Add Courses | 3. Input Marks | 4. List Courses | 5. List Students | 6. Show Marks | 0. Exit")
    choice = input("Enter your choice: ")
    
    if choice == '1': add_students()
    elif choice == '2':add_course()
    elif choice == '3': input_marks()
    elif choice == '4': list_course()
    elif choice == '5': list_students()
    elif choice == '6': show_marks()
    elif choice == '0': 
        print("Exiting program...")
        break
    else: 
        print("Invalid choice. Please try again.")
        
