n = int(input())
command_even = 'even'
command_odd = 'odd'
command_negative = 'negative'
command_positive = 'positive'
numbers = []
filtered = []

for _ in range(n):
    current_number = int(input())
    numbers.append(current_number)

command = input()
for num in numbers:
    filter_command = (
        (command == command_even and num % 2 == 0) or
        (command == command_odd and num % 2 == 1) or
        (command == command_negative and num < 0) or
        (command == command_positive and num >= 0)
    )
    if filter_command:   # is True
        filtered.append(num)
print(filtered)





n = int(input())

numbers = []
filtered = []

for _ in range(n):
    current_number = int(input())
    numbers.append(current_number)

command = input()
if command == "even":
   for num in numbers:
       if num % 2 == 0:
           filtered.append(num)
elif command == "odd":
   for num in numbers:
       if num % 2 == 1:
           filtered.append(num)
elif command == "negative":
   for num in numbers:
       if num < 0:
           filtered.append(num)
elif command == "positive":
   for num in numbers:
       if num >= 0:
           filtered.append(num)

print(filtered)
