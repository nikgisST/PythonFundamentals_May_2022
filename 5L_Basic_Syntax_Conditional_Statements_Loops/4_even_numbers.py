number_of_lines = int(input())

for _ in range(number_of_lines):
    current_number = int(input())
    if current_number % 2 != 0:
        print(f"{current_number} is odd!")
        break
else:
    print("All numbers are even.")





number_of_lines = int(input())
for _ in range(number_of_lines):
    current_number = int(input())
    if current_number % 2 != 0:
        print(f"{current_number} is odd!")
else:
    print("All numbers are even.")




number_of_lines = int(input())
is_odd = False
odd_number = 0
for _ in range(number_of_lines):
    current_number = int(input())
    if current_number % 2 != 0:
        odd_number = current_number
        is_odd = True
        break
if is_odd:
    print(f"{odd_number} is odd!")
else:
    print("All numbers are even.")