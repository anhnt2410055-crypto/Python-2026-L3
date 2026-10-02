import math

# ==========================================
# 1. DEFINE THE STUDENT CLASS
# ==========================================
class Student:
    def __init__(self, name):
        self.name = name
        self.marks = [] # This will store tuples like (mark, credit)

    def add_mark(self, mark, credit):
        # Using math.floor() as requested in the assignment
        # This rounds down to 1 decimal place
        rounded_mark = math.floor(mark * 10) / 10
        self.marks.append((rounded_mark, credit))

    def calculate_gpa(self):
        if not self.marks:
            return 0.0
        
        # Pure Python weighted sum (no numpy needed)
        total_weighted_score = sum(m * c for m, c in self.marks)
        total_credits = sum(c for m, c in self.marks)
        
        if total_credits == 0:
            return 0.0
            
        return total_weighted_score / total_credits

# ==========================================
# 2. CREATE STUDENTS AND ADD MARKS
# ==========================================
student1 = Student("Alice")
student1.add_mark(8.55, 3) # Will round down to 8.5
student1.add_mark(7.0, 2)

student2 = Student("Bob")
student2.add_mark(9.0, 4)
student2.add_mark(6.5, 3)

# ==========================================
# 3. LIST AND SORT BY GPA (Descending)
# ==========================================
students = [student1, student2]


students_sorted = sorted(students, key=lambda s: s.calculate_gpa(), reverse=True)
print("--- Sorted Students by GPA ---")
for s in students_sorted:
    print(f"Name: {s.name} | GPA: {s.calculate_gpa():.2f}")