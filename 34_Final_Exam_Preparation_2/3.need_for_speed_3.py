cars_dictionary = {'mileage': 0, 'fuel': 20}
#cars_dictionary = ['mileage', 'fuel']
cars_dictionary['mileage'] += 100
print(cars_dictionary['mileage'])
print(cars_dictionary)



def create_cars_information(cars_dictionary, number):
    for _ in range(number):
        data = input().split("|")
        brand = data[0]
        mileage = int(data[1])
        fuel = int(data[2])
        cars_dictionary[brand] = [mileage, fuel]
        #if brand not in cars_dictionary:
            #cars_dictionary[brand] = {'mileage': [], 'fuel': []}
    return cars_dictionary


def additional_cars_data(cars_dictionary):
    while True:
        command = input()
        if command == 'Stop':
            break
        command = command.split(' : ')
        type_of_command = command[0]
        brand = command[1]

        if type_of_command == "Drive":
            distance = int(command[2])
            fuel = int(command[3])
            available_fuel = cars_dictionary[brand][1]
            current_mileage = cars_dictionary[brand][0]
            if available_fuel < fuel:
                print("Not enough fuel to make that ride")
            else:
                cars_dictionary[brand][1] -= fuel
                cars_dictionary[brand][0] += distance
                print(f"{brand} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if cars_dictionary[brand][0] >= 100000:
                del cars_dictionary[brand]
                print(f"Time to sell the {brand}!")

        elif type_of_command == "Refuel":
            fuel = int(command[2])
            available_fuel = cars_dictionary[brand][1]
            if fuel + available_fuel > 75:
                fuel = 75 - available_fuel
            cars_dictionary[brand][1] += fuel
            print(f"{brand} refueled with {fuel} liters")

        elif type_of_command == "Revert":
            kilometers = int(command[2])
            current_mileage = cars_dictionary[brand][0]
            if current_mileage - kilometers < 10000:
                cars_dictionary[brand][0] = 10000
            else:
                cars_dictionary[brand][0] -= kilometers
                print(f"{brand} mileage decreased by {kilometers} kilometers")

    return cars_dictionary


def print_function(cars_dictionary):
    for current_brand in cars_dictionary:
        mileage = cars_dictionary[current_brand][0]
        fuel = cars_dictionary[current_brand][1]
        print(f"{current_brand} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.")


def need_for_speed(number):
    # the current dictionary contains a list with two values
    # at index 0 we have mileage, and at index 1 we have fuel
    cars_dictionary = {}
    create_cars_information(cars_dictionary,number)
    additional_cars_data(cars_dictionary)
    print_function(cars_dictionary)


n = int(input())
need_for_speed(n)





def create_cars_information(cars_dictionary, number):
    for _ in range(number):
        data = input().split("|")
        name_of_car = data[0]
        mileage = int(data[1])
        fuel = int(data[2])
        cars_dictionary[name_of_car] = {'mileage': mileage, 'fuel': fuel}
    return cars_dictionary


def additional_cars_data(cars_dictionary):
    while True:
        command = input().split(' : ')
        if command[0] == 'Stop':
            break
        type_of_command = command[0]
        name_of_car = command[1]

        if type_of_command == "Drive":
            distance = int(command[2])
            fuel = int(command[3])
            if cars_dictionary[name_of_car]['fuel'] < fuel:
                print("Not enough fuel to make that ride")
            else:
                cars_dictionary[name_of_car]['mileage'] += distance
                cars_dictionary[name_of_car]['fuel'] -= fuel
                print(f"{name_of_car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if cars_dictionary[name_of_car]['mileage'] >= 100000:
                del cars_dictionary[name_of_car]
                print(f"Time to sell the {name_of_car}!")

        elif type_of_command == "Refuel":
            fuel = int(command[2])
            if cars_dictionary[name_of_car]['fuel'] + fuel > 75:
                fuel = 75 - cars_dictionary[name_of_car]['fuel']
                cars_dictionary[name_of_car]['fuel'] = 75
            else:
                cars_dictionary[name_of_car]['fuel'] += fuel
            print(f"{name_of_car} refueled with {fuel} liters")

        elif type_of_command == "Revert":
            kilometers = int(command[2])
            cars_dictionary[name_of_car]['mileage'] -=kilometers
            if cars_dictionary[name_of_car]['mileage'] < 10000:
                cars_dictionary[name_of_car]['mileage'] = 10000
                continue
            print(f"{name_of_car} mileage decreased by {kilometers} kilometers")

    return cars_dictionary


def print_function(cars_dictionary):
    for current_brand in cars_dictionary:
        mileage = cars_dictionary[current_brand]['mileage']
        fuel = cars_dictionary[current_brand]['fuel']
        print(f"{current_brand} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.")


def need_for_speed(number):
    cars_dictionary = {}
    create_cars_information(cars_dictionary,number)
    additional_cars_data(cars_dictionary)
    print_function(cars_dictionary)


n = int(input())
need_for_speed(n)
