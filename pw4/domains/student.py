import math

class Student:
    def __init__(self, name):
        self.name = name
        self.marks = [] # List of tuples: (mark, credit)

    def add_mark(self, mark, credit):
        rounded_mark = math.floor(mark * 10) / 10
        self.marks.append((rounded_mark, credit))

    def calculate_gpa(self):
        if not self.marks:
            return 0.0
        total_weighted_score = sum(m * c for m, c in self.marks)
        total_credits = sum(c for m, c in self.marks)
        if total_credits == 0:
            return 0.0
        return total_weighted_score / total_credits