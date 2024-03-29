force_side_dict = {}
command = input()
while command != "Lumpawaroo":
    if "|" in command:
        split_command = command.split(" | ")
        force_side, force_user = split_command[0], split_command[1]
        present = False
        for value in force_side_dict.values():
            if force_user in value:
                present = True
                break
        if not present:
            if force_side not in force_side_dict.keys():
                force_side_dict[force_side] = []
            force_side_dict[force_side].append(force_user)

    elif "->" in command:
        split_command = command.split(" -> ")
        force_side, force_user = split_command[1], split_command[0]
        for key, value in force_side_dict.items():
            if force_user in value:
                force_side_dict[key].pop(value.index(force_user))
                break
        if force_side not in force_side_dict.keys():
            force_side_dict[force_side] = []
        force_side_dict[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")

    command = input()

for force_side in force_side_dict.keys():
    if len(force_side_dict[force_side]) > 0:
        print(f"Side: {force_side}, Members: {len(force_side_dict[force_side])}")
        [print(f"! {user}") for user in force_side_dict[force_side]]