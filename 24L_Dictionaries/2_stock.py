elements = input().split(" ")
bakery = {elements[i]: int(elements[i+1]) for i in range(0, len(elements), 2)}

searched_products = input().split()

for product in searched_products:
    if product in bakery:
        print(f"We have {bakery[product]} of {product} left")
    elif product not in bakery:
        print(f'Sorry, we don\'t have {product}')