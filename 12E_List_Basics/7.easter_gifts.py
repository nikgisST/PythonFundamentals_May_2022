gifts_names = input().split()

while True:
    command = input()
    if "No Money" in command:
        break
    elif "OutOfStock" in command:
        command_list = command.split()
        gifts_names = ["None" if gifts_names[i] == command_list[1] else gifts_names[i]
                       for i in range(len(gifts_names))]
    elif "Required" in command:
        command_list = command.split()
        gifts_names = [command_list[1] if i == int(command_list[2]) else gifts_names[i]
                       for i in range(len(gifts_names))]
    elif "JustInCase" in command:
        command_list = command.split()
        gifts_names = [command_list[1] if gifts_names[i] == gifts_names[-1] else gifts_names[i]
                       for i in range(len(gifts_names))]

gifts_names = [gifts_names[i] for i in range(len(gifts_names)) if not gifts_names[i] == "None"]
gifts_names = ' '.join([str(i) for i in gifts_names])

print(gifts_names)

gifts_list = input().split(" ")
command = input()

while not command == 'No Money':
    if 'OutOfStock' in command:
        command, gift = command.split(" ")
        for current_gift in range(len(gifts_list)):
            if gifts_list[current_gift] == gift:
                gifts_list[current_gift] = 'None'
    elif 'Required' in command:
        command, gift, index = command.split(" ")
        index = int(index)
        if 0 < index < len(gifts_list):
            gifts_list[index] = gift
    elif 'JustInCase' in command:
        command, gift = command.split(" ")
        gifts_list[-1] = gift
    command = input()

for gifts in range(len(gifts_list)):
    if 'None' in gifts_list:
        gifts_list.remove('None')
print(' '.join(gifts_list))