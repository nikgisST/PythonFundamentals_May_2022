product_price = {}
product_qty = {}

while True:
    command = input()
    if command == "buy":
        break

    product_data = command.split(" ")
    product = product_data[0]
    price = float(product_data[1])
    qty = int(product_data[2])

    if product not in product_qty:
        product_qty[product] = qty
    else:
        product_qty[product] += qty
    product_price[product] = price

for product, price in product_price.items():
    total_price = price * product_qty[product]
    print(f"{product} -> {total_price:.2f}")




products = {}
while True:
    line = input()
    if line == "buy":
        break

    product_name, price, quantity = line.split()
    price = float(price)
    quantity = int(quantity)

    if product_name in products:
        products[product_name]['quantity'] += quantity
        if products[product_name]['price'] != price:
            products[product_name]['price'] = price
    else:
        products[product_name] = {'price': price, 'quantity': quantity}

for product_name, product_info in products.items():
    total_price = product_info['price'] * product_info['quantity']
    print(f"{product_name} -> {total_price:.2f}")
