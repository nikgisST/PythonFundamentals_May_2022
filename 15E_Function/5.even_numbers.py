numbers_as_string = input().split()
numbers_as_digits = []
for current_number in numbers_as_string:
    numbers_as_digits.append(int(current_number))

#numbers_as_digits = [int(s) for s in input().split() if int(s) % 2 == 0]

is_even = lambda x: x % 2 == 0
result = list(filter(is_even, numbers_as_digits))
print(result)


----------------------------------------------------------------------

def is_even(number: int):
    if int(number) % 2 == 0:
        return True
    return False

#def is_even(number):
    #if number % 2 == 0:
        #return True
    #return False

numbers = input().split()
filtered_numbers = []
for current_number in numbers:
    if is_even(current_number):                         #if is_even(current_number) == True:
        filtered_numbers.append(int(current_number))
print(filtered_numbers)