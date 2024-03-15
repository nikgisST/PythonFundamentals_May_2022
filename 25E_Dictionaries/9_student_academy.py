n = int(input())
students_grades = {}

for _ in range(n):
    student = input()
    grade = float(input())

    if student not in students_grades:
        students_grades[student] = []
    students_grades[student].append(grade)

filtered_students = {}
for student, grades in students_grades.items():
    avg_grade = sum(grades) / len(grades)
    if avg_grade >= 4.50:
        filtered_students[student] = avg_grade

for name, grade in sorted(filtered_students.items(), key=lambda x: x[1], reverse=True):
    print(f"{name} -> {grade:.2f}")





students_data = {}
average_grade_data = {}

for _ in range(num_students):
    student = input()
    grade = float(input())
    if student not in students_data:
        students_data[student] = [grade]
    else:
        students_data[student].append(grade)

for student, grade in students_data.items():
    average_grade = sum(grade) / len(grade)
    if average_grade >= 4.5:
        average_grade_data[student] = average_grade

filtered_students = sorted(average_grade_data.items(), key=lambda x: -x[1])
for student, grade in filtered_students:
    print(f"{student} -> {grade:.2f}")




students = int(input())
students_grades = {}
for current_student in range(students):
    student_name = input()
    grade = float(input())
    if student_name not in students_grades:
        students_grades[student_name] = grade
    elif student_name in students_grades:
        list_grades = [students_grades[student_name], grade]
        students_grades[student_name] = list_grades

for student, grades in students_grades.items():
    if type(grades) == list:
        average_grade = sum(grades) / len(grades)
    else:
        average_grade = grades
    if average_grade >= 4.5:
        print(student, f'-> {average_grade:.2f}')