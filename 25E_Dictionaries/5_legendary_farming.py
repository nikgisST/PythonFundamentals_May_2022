useful_items = {"shards": 0, "fragments": 0, "motes": 0}
got_obtained = False
command = input().split()
while not got_obtained:
    for index in range(0, len(command), 2):
        value = int(command[index])
        key = command[index + 1].lower()
        if key not in useful_items.keys():
            useful_items[key] = 0
        useful_items[key] += value
        if useful_items["shards"] >= 250:
            print("Shadowmourne obtained!")
            useful_items["shards"] -= 250
            got_obtained = True
        elif useful_items["fragments"] >= 250:
            print("Valanyr obtained!")
            useful_items["fragments"] -= 250
            got_obtained = True
        elif useful_items["motes"] >= 250:
            print("Dragonwrath obtained!")
            useful_items["motes"] -= 250
            got_obtained = True
        if got_obtained:
            break
    if got_obtained:
        break

    command = input().split()

for material, quantity in useful_items.items():
    print(f"{material}: {quantity}")






useful_items = {"shards": 0, "fragments": 0, "motes": 0}
useless_items = {}
got_obtained = False
command = input().split()
while True:
    for index in range(0, len(command), 2):
        value = int(command[index])
        key = command[index + 1].lower()
        if key == "shards" or key == "fragments" or key == "motes":    # if key in useful_items:
            useful_items[key] += value
        else:
            if key not in useless_items.keys():     #in useless_items:
                useless_items[key] = 0
            useless_items[key] += value
        if useful_items["shards"] >= 250:
            print("Shadowmourne obtained!")
            useful_items["shards"] -= 250
            got_obtained = True
        elif useful_items["fragments"] >= 250:
            print("Valanyr obtained!")
            useful_items["fragments"] -= 250
            got_obtained = True
        elif useful_items["motes"] >= 250:
            print("Dragonwrath obtained!")
            useful_items["motes"] -= 250
            got_obtained = True
        if got_obtained:
            break
    if got_obtained:
        break

    command = input().split()

for material, quantity in useful_items.items():
    print(f"{material}: {quantity}")

for material, quantity in useless_items.items():
    print(f"{material}: {quantity}")

