train_length = int(input())
wagons = [0] * train_length
command = input()
while command != "End":
    tokens = command.split(" ")
    key_word = tokens[0]
    if key_word == "add":
        people_to_add = int(tokens[1])
        wagons[-1] += people_to_add
    elif key_word == "insert":
        index = int(tokens[1])
        number_of_people = int(tokens[2])
        wagons[index] += number_of_people
    elif key_word == "leave":
        index = int(tokens[1])
        number_of_people = int(tokens[2])
        wagons[index] -= number_of_people

    command = input()

print(wagons)





train_length = int(input())
wagons = [0] * train_length
while True:
    command = input()
    if command == 'End':
        break
    data = command.split(" ")
    key_word = data[0]
    if key_word == "add":
        people_to_add = data[1]
        wagons[-1] += int(people_to_add)
    elif key_word == "insert":
        index = int(data[1])
        number_of_people = int(data[2])
        wagons[index] += number_of_people
    elif key_word == "leave":
        index = int(data[1])
        number_of_people = int(data[2])
        wagons[index] -= number_of_people
print(wagons)
