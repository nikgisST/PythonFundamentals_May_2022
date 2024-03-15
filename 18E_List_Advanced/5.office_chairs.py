def check_chairs(given_number_of_rooms):
    func_total_free_chairs, func_needed_chairs = 0, 0
    # total_free_chairs = 0
    # needed_chairs = 0
    for current_room_number in range(1, given_number_of_rooms + 1):
        free_chairs, visitors = input().split()                      #И ДВАТА ЕЛЕМЕНТА СЕ НАМИРАТ В ЕДИН ЛИСТ ТАКА
        difference = len(free_chairs) - int(visitors)
        if difference >= 0:
            func_total_free_chairs += difference
        else:
            func_needed_chairs += abs(difference)
            print(f"{abs(difference)} more chairs needed in room {current_room_number}")
    return func_total_free_chairs, func_needed_chairs


number_of_rooms = int(input())
total_free_chairs, needed_chairs = check_chairs(number_of_rooms)
if total_free_chairs >= needed_chairs:
    print(f"Game On, {total_free_chairs} free chairs left")


# CTRL + ALT + SHIFT = MULTIPLE LINES SELECTED AND WRITABLE IN THE SAME TIME


def something():
    return 5,6,7,8
a,b,c,d = something()
print(a,b,c,d)


def something():
    return 5,6,7,8
a = something()
print(a)                  # ВРЪЩА ТАКА tuple : (5, 6, 7, 8)


def something(numbers):
    return numbers[::-1]
some_numbers = [1,2,3,4,5]
result = something(some_numbers)
print(result)

