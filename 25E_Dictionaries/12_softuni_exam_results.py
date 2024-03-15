exam_languages = {}
exam_results = {}

while True:
    command = input()
    if command == "exam finished":
        break

    exam_data = command.split("-")
    if len(exam_data) == 3:
        [user, language, points] = exam_data
        points = int(points)
        if user not in exam_results:
            exam_results[user] = points
        else:
            if exam_results[user] <= points:
                exam_results[user] = points
            else:
                exam_results[user] = exam_results[user]
        if language not in exam_languages:
            exam_languages[language] = 1
        else:
            exam_languages[language] += 1
    else:
        [user, _] = exam_data
        exam_results.pop(user)

print("Results:")

filtered_results = sorted(exam_results.items(), key=lambda x: (-x[1], x[0]))

for user, points in filtered_results:
    print(f"{user} | {points}")

print(f"Submissions:")

filtered_languages = sorted(exam_languages.items(), key=lambda x: (-x[1], x[0]))

for language, count in filtered_languages:
    print(f"{language} - {count}")






data = input()
language_submissions = {}
students_scores = {}

while not data == "exam finished":

    if "banned" in data:
        username = data.split("-")[0]
        del students_scores[username]

    else:
        username, language, points = data.split("-")
        points = int(points)
        if username not in students_scores:
            students_scores[username] = []
        students_scores[username].append(points)

        if language not in language_submissions:
            language_submissions[language] = 0
        language_submissions[language] += 1

    data = input()

for student, score in students_scores.items():
    students_scores[student] = max(score)

print("Results:")
for student, score in sorted(students_scores.items(), key=lambda x: (-x[1], x[0])):
    print(f"{student} | {score}")

print("Submissions:")
for language, count in sorted(language_submissions.items(), key=lambda x: (-x[1], x[0])):
    print(f"{language} - {count}")