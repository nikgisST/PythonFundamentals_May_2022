numbers = input().split()
n_removes = int(input())
numbers_list = [int(numbers[i]) for i in range(len(numbers))]

for removes in range(n_removes):
    numbers_list.remove(min(numbers_list))

print(numbers_list)




numbers = input().split()
n_remove = int(input())
numbers_int = [int(num) for num in numbers]

for i in range(n_remove):
    numbers_int.remove(min(numbers_int))

print(numbers_int)




list_numbers = input().split()
remover = int(input())
big_numbers = []

for number in list_numbers:
    big_numbers.append(int(number))

for removing in range(remover):
    big_numbers.remove(min(big_numbers))

print(*big_numbers, sep=', ')
