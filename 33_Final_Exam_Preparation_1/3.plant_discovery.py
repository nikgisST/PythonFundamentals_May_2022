def create_plants_information(plants_dictionary, number):
    for _ in range(number):
        data = input().split("<->")
        name_of_plant = data[0]
        rarity = data[1]
        #plants_dictionary[name_of_plant] = {'rarity': rarity, 'rating': []}
        if name_of_plant not in plants_dictionary:
            plants_dictionary[name_of_plant] = {'rarity': rarity, 'rating': []}
        else:
            plants_dictionary[name_of_plant]['rarity'] = rarity
    return plants_dictionary


def additional_plants_data(plants_dictionary):
    while True:
        command = input().split(': ')
        if command[0] == 'Exhibition':
            break
        data = command[1].split(' - ')
        type_of_command = command[0]
        plant = data[0]
        if plant not in plants_dictionary:
            print('error')
            continue

        if type_of_command == "Rate":
            rating = int(data[1])
            plants_dictionary[plant]['rating'].append(rating)

        elif type_of_command == "Update":
            new_rarity = int(data[1])
            plants_dictionary[plant]['rarity'] = new_rarity

        elif type_of_command == "Reset":
            plants_dictionary[plant]['rating'].clear()
    return plants_dictionary


def print_function(plants_dictionary):
    print('Plants for the exhibition:')
    for current_plant in plants_dictionary:
        if len(plants_dictionary[current_plant]["rating"]) > 0 and sum(plants_dictionary[current_plant]["rating"]) > 0:
            average_rating = sum(plants_dictionary[current_plant]["rating"]) / len(plants_dictionary[current_plant]["rating"])
        else:
            average_rating = 0
        rarity = plants_dictionary[current_plant]["rarity"]
        print(f"- {current_plant}; Rarity: {rarity}; Rating: {average_rating:.2f}")


def plant_discovery(number):
    plants_dictionary = {}
    create_plants_information(plants_dictionary,number)
    additional_plants_data(plants_dictionary)
    print_function(plants_dictionary)


n = int(input())
plant_discovery(n)