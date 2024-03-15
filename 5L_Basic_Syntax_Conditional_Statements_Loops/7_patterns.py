number = int(input())
for rows in range(1, number + 1):
    for columns in range(0, rows):
        print("*", end="")
    print()
for rows in range(number - 1, 0, -1):
    for columns in range(0, rows):
        print("*", end="")
    print()



number_of_stars = int(input())
for i in range(1, number_of_stars + 1):
    print(i * "*")
for j in range(number_of_stars - 1, 0, -1):
    print(j * "*")



number_of_stars = int(input())
for i in range(1, number_of_stars + 1):
    print(i * "*")
for j in range(number_of_stars - 1, -1, -1):
    print(j * "*")