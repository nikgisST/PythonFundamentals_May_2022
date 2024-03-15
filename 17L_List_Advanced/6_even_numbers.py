numbers = list(map(int, input().split(', ')))
#print(numbers)
indices = [i for i in range(len(numbers)) if numbers[i] % 2 == 0]
print(indices)





numbers = list(map(int, input().split(', ')))
found_indices_or_no = map(lambda i: i if numbers[i] % 2 == 0 else 'no', range(len(numbers)))
indices = list(filter(lambda x: x != 'no', found_indices_or_no))
print(indices)