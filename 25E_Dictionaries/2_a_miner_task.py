resource = {}
while True:
    current_resource = input()
    if current_resource == "stop":
        break
    #current_resource = current_resource.lower()
    quantity = int(input())
    if current_resource not in resource.keys():
        resource[current_resource] = 0
    resource[current_resource] += quantity
for resource, quantity in resource.items():
    print(f"{resource} -> {quantity}")
    #print(f"{resource.capitalize()} -> {quantity}")