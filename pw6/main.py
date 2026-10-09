import csv
import statistics

def load_csv(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return list(csv.DictReader(f))

print("========== DATA MANIPULATION ==========")
students = load_csv('students.csv')

print("\n--- 1. First 5 rows ---")
for i in range(5):
    print(students[i])

print(f"\n--- 2. Rows and Columns ---")
print(f"Rows: {len(students)}")
print(f"Columns: {len(students[0])}")

valid_gpas = [float(s['GPA']) for s in students if s['GPA']]
avg_gpa = sum(valid_gpas) / len(valid_gpas)

for s in students:
    if not s['GPA']:
        s['GPA'] = str(round(avg_gpa, 2))

print("\n--- 3. Name and GPA ---")
for s in students:
    print(f"{s['name']}: {s['GPA']}")

print("\n--- 4. Students with GPA >= 3.5 ---")
for s in students:
    if float(s['GPA']) >= 3.5:
        print(f"{s['name']} ({s['GPA']})")

print("\n--- 5. Sorted by GPA (Descending) ---")
sorted_students = sorted(students, key=lambda x: float(x['GPA']), reverse=True)
for s in sorted_students[:10]: # In 10 bạn đầu cho đỡ dài
    print(f"{s['name']}: {s['GPA']}")

print("\n--- 6. Average GPA by Major ---")
majors = {}
for s in students:
    major = s['major']
    if major not in majors:
        majors[major] = []
    majors[major].append(float(s['GPA']))

for major, gpas in majors.items():
    print(f"{major}: {statistics.mean(gpas):.2f}")


print("\n========== RAW DATA TO USEFUL INFO ==========")
students_part2 = load_csv('students.csv')
scores_part2 = load_csv('scores.csv')

print("\n--- Check Missing Values ---")
missing_found = False
for row in scores_part2:
    missing = [k for k, v in row.items() if v == '']
    if missing:
        missing_found = True
        print(f"Student {row['student_id']} missing: {missing}")
if not missing_found:
    print("No missing values found.")

py_scores = [float(s['python']) for s in scores_part2 if s['python']]
math_scores = [float(s['math']) for s in scores_part2 if s['math']]
db_scores = [float(s['database']) for s in scores_part2 if s['database']]

avg_py = sum(py_scores) / len(py_scores)
avg_math = sum(math_scores) / len(math_scores)
avg_db = sum(db_scores) / len(db_scores)

for s in scores_part2:
    if not s['python']: s['python'] = str(round(avg_py, 2))
    if not s['math']: s['math'] = str(round(avg_math, 2))
    if not s['database']: s['database'] = str(round(avg_db, 2))

merged_data = []
for s in students_part2:
    for sc in scores_part2:
        if s['student_id'] == sc['student_id']:
            combined = {**s, **sc}
            avg_score = (float(sc['python']) + float(sc['math']) + float(sc['database'])) / 3
            combined['average_score'] = round(avg_score, 2)
            merged_data.append(combined)
            break

top_5 = sorted(merged_data, key=lambda x: x['average_score'], reverse=True)[:5]
print("\n--- Top 5 Students by Average Score ---")
for s in top_5:
    print(f"{s['name']}: {s['average_score']}")

print("\n--- Average Score by Major ---")
major_scores = {}
for s in merged_data:
    major = s['major']
    if major not in major_scores:
        major_scores[major] = []
    major_scores[major].append(s['average_score'])

for major, scores_list in major_scores.items():
    print(f"{major}: {statistics.mean(scores_list):.2f}")