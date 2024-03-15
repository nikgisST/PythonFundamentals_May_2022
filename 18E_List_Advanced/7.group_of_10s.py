numbers = list(map(int, input().split(', ')))

for group in range(1, 11):
    if len(numbers) == 0:
        break
    group_list = [num for num in numbers if num <= (group * 10)]
    numbers = [num for num in numbers if num not in group_list]
    print(f"Group of {group}0's: {group_list}")





numbers = [int(n) for n in input().split(", ")]
boundary = 0

while numbers:
    boundary += 10
    current_group = []
    for num in numbers:
        if num <= boundary:
            current_group.append(num)
    for num in current_group:
        numbers.remove(num)

    print(f"Group of {boundary}'s: {current_group}")