list_of_events = input().split("|")
total_energy = 100
total_coins = 100
bakery_is_open = True
for event in list_of_events:
    event_info = event.split("-")
    type_of_event = event_info[0]
    number =int(event_info[1])
    if type_of_event == "rest":
        temporary_energy = total_energy
        total_energy += number
        if total_energy > 100:
            total_energy = 100
        gained_energy = total_energy - temporary_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {total_energy}.")
    elif type_of_event == "order":
        if total_energy >= 30:
            total_energy -= 30
            total_coins += number
            print(f"You earned {number} coins.")
        else:
            total_energy += 50
            print(f"You had to rest!")
    else:
        if total_coins >= number:
            total_coins -= number
            print(f"You bought {type_of_event}.")
        else:
            print(f"Closed! Cannot afford {type_of_event}.")
            bakery_is_open = False
            break
if bakery_is_open:   #if bakery_is_oper == True:
    print(f"Day completed!")
    print(f"Coins: {total_coins}")
    print(f"Energy: {total_energy}")

# min_number = min(list)    max(list)
# list.remove(min_number)