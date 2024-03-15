# data = input().split(" ")
# products_dict = {}
# for i in range(0, len(data), 2):
#     products_dict[data[i]] = int(data[i + 1])
# print(products_dict)



data = input().split()
products_dict = dict()
for i in range(0, len(data), 2):
    key = data[i]
    value = data[i + 1]
    products_dict[key] = int(value)
print(products_dict)




# data = input().split(" ")
# products_dict = {data[i]: int(data[i + 1]) for i in range(0, len(data), 2)}
# print(products_dict)