def shoot_func(index, power, first_target):
    if 0 <= index < len(first_target):
        if first_target[index] - power <= 0:
            first_target.pop(index)
        else:
            first_target[index] -= power
    return first_target


def add_func(index, value, second_target):
    if 0 <= index < len(second_target):
        second_target.insert(index, value)
    else:
        print("Invalid placement!")
    return second_target


def strike_func(index, radius, third_target):
    validator_index = index - radius >= 0 and index + radius < len(third_target)
    if validator_index:
        start_target_index = index - radius
        end_target_index = index + radius
        third_target = [third_target[i] for i in range(len(third_target)) if i < start_target_index or i > end_target_index]

    elif not validator_index:
        print("Strike missed!")
    return third_target


def moving_target(targets):
    while True:
        command = input()
        if command == 'End':
            print("|".join([str(num) for num in targets]))
            break
        command = command.split(' ')
        current_command = command[0]
        first_element = int(command[1])
        second_element = int(command[2])
        if current_command == 'Shoot':
            targets = shoot_func(first_element, second_element, targets)
        elif current_command == 'Add':
            targets = add_func(first_element, second_element, targets)
        elif current_command == 'Strike':
            targets = strike_func(first_element, second_element, targets)


data = list(map(int, input().split(" ")))
moving_target(data)
