course = input().split(', ')
command = input()
while not command == 'course start':
    command = command.split(':')
    lesson = command[1]

    if command[0] == 'Add':
        if lesson not in course:
            course.append(lesson)

    elif command[0] == 'Insert':
        index = int(command[2])
        if lesson not in course:
            course.insert(index, lesson)

    elif command[0] == 'Remove':
        to_remove = f"{lesson}-Exercise"
        if lesson in course:
            course.remove(lesson)
        if to_remove in course:
            course.remove(to_remove)

    elif command[0] == 'Swap':
        lesson1 = command[1]
        lesson2 = command[2]
        if lesson1 in course and lesson2 in course:
            modified_course = []
            for lesson in course:
                if lesson == lesson1:
                    modified_course.append(lesson2)
                elif lesson == lesson2:
                    modified_course.append(lesson1)
                else:
                    modified_course.append(lesson)
            course.clear()
            course = modified_course

        if 'Exercise' in lesson:
            for index in range(len(course)):
                if course[index] == lesson2:
                    course.remove(lesson)
                    course.insert(index + 1, lesson)
                    break

    elif command[0] == 'Exercise':
        to_add = f"{lesson}-Exercise"
        if lesson not in course:
            course.append(lesson)
            course.append(to_add)
        elif lesson in course and to_add not in course:
            for index in range(len(course)):
                if course[index] == lesson:
                    course.insert(index + 1, to_add)
                    break

    command = input()

counter = 0
for el in range(len(course)):
    counter += 1
    print(f"{counter}.{course[el]}")

data = input().split(', ')
command = input()
while not command == "course start":
    command = command.split(':')
    action = command[0]
    lesson = command[1]
    exercise = f'{lesson}-Exercise'
    if action == 'Add':
        if lesson not in data:
            data.append(lesson)
    elif action == 'Insert':
        index = int(command[2])
        if lesson not in data:
            data.insert(index, lesson)
    elif action == 'Remove':
        if lesson in data:
            data.remove(lesson)
            if exercise in data:
                data.remove(exercise)

    elif action == 'Swap':
        lesson1 = command[1]
        lesson2 = command[2]
        exercise1 = f'{lesson1}-Exercise'
        exercise2 = f'{lesson2}-Exercise'
        if lesson1 in data and lesson2 in data:
            index1 = data.index(lesson1)
            index2 = data.index(lesson2)
            data[index1], data[index2] = data[index2], data[index1]

        if exercise2 in data:
            data.remove(exercise2)
            data.insert(data.index(lesson2) + 1, exercise2)

        elif exercise1 in data:
            data.remove(exercise1)
            data.insert(data.index(lesson1) + 1, exercise1)

    elif action == 'Exercise':
        if lesson in data:
            if exercise not in data:
                lesson_index = data.index(lesson)
                data.insert(lesson_index + 1, exercise)
        else:
            data.append(lesson)
            data.append(exercise)

    command = input()

for el in range(1, len(data) + 1):
    print(f'{el}.{data[el - 1]}')