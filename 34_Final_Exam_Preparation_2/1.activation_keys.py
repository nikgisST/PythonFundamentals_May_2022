def activation_key():
    key = input()

    while True:
        command = input().split(">>>")
        current_command = command[0]

        if current_command == "Generate":
            print(f"Your activation key is: {key}")
            break

        elif current_command == 'Slice':
            start_index = int(command[1])
            end_index = int(command[2])
            key = key[:start_index] + key[end_index:]
            print(key)

        elif current_command == 'Flip':
            start_index = int(command[2])
            end_index = int(command[3])
            if command[1] == 'Upper':
                key = key[:start_index] + key[start_index:end_index].upper() + key[end_index:]
            elif command[1] == 'Lower':
                key = key[:start_index] + key[start_index:end_index].lower() + key[end_index:]
            print(key)

        elif current_command == "Contains":
            substring = command[1]
            if substring in key:
                print(f'{key} contains {substring}')
            else:
                print('Substring not found!')


activation_key()