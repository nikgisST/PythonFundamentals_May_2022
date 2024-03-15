def create_heroes_information(heroes_dictionary, number):
    for _ in range(number):
        data = input().split(" ")
        hero_name = data[0]
        hit_points = int(data[1])
        mana_points = int(data[2])
        heroes_dictionary[hero_name] = [hit_points, mana_points]
        #if hero_name not in heroes_dictionary:
            #heroes_dictionary[hero_name] = {'hit_points': [], 'mana_points': []}
    return heroes_dictionary

def additional_heroes_data(heroes_dictionary):
    while True:
        #command = command.split(' - ')
        command = input()                # после без този ред
        if command == 'End':
            break
        command = command.split(' - ')
        type_of_command = command[0]
        hero_name = command[1]

        if type_of_command == 'CastSpell':
            mp_needed = int(command[2])
            spell_name = command[3]
            available_mp = heroes_dictionary[hero_name][1]
            if available_mp >= mp_needed:
                heroes_dictionary[hero_name][1] -= mp_needed
                current_mp = heroes_dictionary[hero_name][1]
                print(f'{hero_name} has successfully cast {spell_name} and now has {current_mp} MP!')
            else:
                print(f"{hero_name} does not have enough MP to cast {spell_name}!")

        elif type_of_command == 'TakeDamage':
            damage = int(command[2])
            attacker = command[3]
            available_hp = heroes_dictionary[hero_name][0]
            if available_hp - damage > 0:
                heroes_dictionary[hero_name][0] -= damage
                current_hp = heroes_dictionary[hero_name][0]
                print(f'{hero_name} was hit for {damage} HP by {attacker} and now has {current_hp} HP left!')
            else:
                del heroes_dictionary[hero_name]
                print(f"{hero_name} has been killed by {attacker}!")

        elif type_of_command == 'Recharge':
            amount = int(command[2])
            available_mp = heroes_dictionary[hero_name][1]
            if available_mp + amount > 200:
                amount = 200 - available_mp
                heroes_dictionary[hero_name][1] += amount
            else:
                heroes_dictionary[hero_name][1] += amount
            print(f"{hero_name} recharged for {amount} MP!")

        elif type_of_command == 'Heal':
            amount = int(command[2])
            available_hp = heroes_dictionary[hero_name][0]
            if available_hp + amount > 100:
                amount = 100 - available_hp
                heroes_dictionary[hero_name][0] += amount
            else:
                heroes_dictionary[hero_name][0] += amount
            print(f"{hero_name} healed for {amount} HP!")
        # if available_hp + amount > 100:
        #     new_amount = 100 - available_hp
        #     heroes_dictionary[hero_name][0] += new_amount
        #     print(f"{hero_name} healed for {new_amount} HP!")
        # else:
        #     heroes_dictionary[hero_name][0] += amount
        #     print(f"{hero_name} healed for {amount} HP!")

    return heroes_dictionary


def print_function(heroes_dictionary):
    for current_hero in heroes_dictionary:
        print(current_hero)
        print(f'  HP: {heroes_dictionary[current_hero][0]}')
        print(f'  MP: {heroes_dictionary[current_hero][1]}')


def heroes_of_code(number):
    # the current dictionary contains a list with two values
    # at index 0 we have HP, and at index 1 we have MP
    heroes_dictionary = {}
    create_heroes_information(heroes_dictionary,number)
    additional_heroes_data(heroes_dictionary)
    print_function(heroes_dictionary)


n = int(input())
heroes_of_code(n)