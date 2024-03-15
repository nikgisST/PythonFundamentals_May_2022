products = {}
while True:
    command = input()
    if command == 'statistics':
        break
    command = command.split(": ")
    product = command[0]
    quantity = int(command[1])
    if product not in products:
        products[product] = quantity
    elif product in products:
        products[product] += quantity
print(f"Products in stock:")
print("\n".join([f"- {item}: {str(products[item])}" for item in products]))
print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")



products = {}
command = input()
while command != "statistics":
    command = command.split(": ")
    product = command[0]
    quantity = int(command[1])
    if product not in products:
        products[product] = 0
    products[product] += quantity
    command = input()
print(f"Products in stock:")
product_representation = [f"- {item}: {str(products[item])}" for item in products]
print("\n".join(product_representation))
print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")




products = {}
command = input()
while command != "statistics":
    command = command.split(": ")
    product = command[0]
    quantity = int(command[1])
    if product not in products:
        products[product] = 0
        products[product] += quantity
    elif product in products:
        products[product] += quantity
    command = input()
print(f"Products in stock:")
#[print(f'- {product}: {quantity}') for product, quantity in products.items()]
for (product, quantity) in products.items():                                     # може и без скобите
    print(f"- {product}: {quantity}")
print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")
