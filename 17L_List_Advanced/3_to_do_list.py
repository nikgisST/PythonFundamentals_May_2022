tasks = []
while True:
    command = input().split("-")
    if command[0] == "End":
        break
    priority = int(command[0])
    task = command[1]
    tasks.append((priority, task))
sorted_tasks = [task_data[1] for task_data in sorted(tasks)]
print(sorted_tasks)




notes = [0] * 10
while True:
    command = input()
    if command == "End":
        break
    tokens = command.split("-")
    priority = int(tokens[0]) - 1
    note = tokens[1]
    notes.pop(priority)
    notes.insert(priority, note)
result = [element for element in notes if element != 0]
print(result)

